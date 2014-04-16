#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdlib.h> 
// wget http://bigota.miwifi.com/xiaoqiang/rom/brcm4709_hdk_0027c_0.4.38.bin
// ./unpack brcm4709_hdk_0027c_0.4.38.bin
// ext4.rootfs.lzma , then use unlzma unpack 
// kernel.trx 4709 kernel trx 
int main(int argv, char *argc[])

{
	int start = 0x20;
	char HDR0[4] = "HDR0";
	struct stat sb;
	//int fd = open("brcm4709_hdk_0027c_0.4.38.bin",O_RDONLY);
	int fd = open(argc[1],O_RDONLY);
	fstat(fd, &sb);
	void  *addr;
	int len = sb.st_size-start;
	addr  = mmap(NULL, sb.st_size, PROT_READ, MAP_SHARED, fd, 0);
	if(addr){
		printf("mmap secuss\n");
	} else{
		close(fd);
		return -1;
	}
	char  *buf ;

	buf = malloc(4);
	int file1 = open("ext4.rootfs.lzma",O_RDWR|O_CREAT);
	char  *ptr;
	ptr = addr;
	ptr += start;
	char *ptr0= ptr;	
	int pad= 16;
	for (int i= 0;i <len-256-pad;i++)
	{
		memset((void *)buf,0,4);
		memcpy(buf, ptr ,4);
		if (strncmp(buf,HDR0,4) ==0){
			write(file1, ptr0, i);
			int kfd = open("kernel.trx",O_RDWR|O_CREAT);
			write(kfd, ptr, len-256-i-pad);
			close(kfd);
			printf("find %s, %d\n",HDR0,i);
		} else {
		   //	write(file1, ptr, size_t nbyte);

		}

		//printf("%X ",*ptr);
		ptr++;
		
	}
	close(file1);
	munmap(addr, len);
	close(fd);
	return 0;
}
