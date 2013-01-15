<?  
$sid=trim($_GET['server']);
switch($sid){
case "1":
    $server="shanghai1";
    break;
case "2":
    $server="shanghai2";
    break;
case "3":
    $server="beijing";
    break;
default:
    echo "Invalid URL!";
    exit(0);
}



  //$connect = mssql_connect("Beijing","gc","CGrand_sega!")or die ("MS-SQL connection failed!"); 
  $connect = mssql_connect($server,"gc","CGrand_sega!")or die ("DB connection failed!"); 
  mssql_select_db("gc"); 
  $num=1440;     

  $qry = "";
  //$qry .= " SELECT TOP 500 SAVETIME, CCUSER          ";
  $qry .= " SELECT TOP $num CCUSER ";
  $qry .= " FROM CONCURRENTUSER   ";
  $qry .= " ORDER BY SAVEKEY DESC ";
  
  $arrayname    = mssql_query($qry,$connect);
  $temp=mssql_fetch_array($arrayname);
  if (!$arrayname) { 
   error("QUERY_ERROR"); 
   exit; 
  }    


$circle=0;

while($row = mssql_fetch_row($arrayname))

{
        $arrayx[$circle]=$row[0];
        $circle++;
}

$nowmax=max($arrayx);
$nowmin=min($arrayx);

mssql_data_seek($temp,0);

$imgwidth=760;
$imgheight=280;
header ("Content-type: image/jpeg");
$im=@imagecreate($imgwidth,$imgheight)
    or die("Cannot Initialize new GD image stream");
$black  = imagecolorallocate($im, 0,    0,  0);
$white  = imagecolorallocate($im, 255,255,255);
$red    = imagecolorallocate($im, 255,  0,  0);
$green  = imagecolorallocate($im, 0,  255,128);
$blue   = imagecolorallocate($im, 0,    0,255);
$yellow = imagecolorallocate($im, 255,255,  0);
$grey   = imagecolorallocate($im, 192,192,192);

imagesetthickness($im,1);
imageantialias ($im,1);

// create the background
// $style = array($red, $red, $red, $red, $red, $white, $white, $white, $white, $white);
// $style = array($blue, $blue, $blue, $blue, $blue, $white, $white, $white, $white, $white);
$style = array($black, $black, $black, $black, $black, $grey, $grey, $grey, $grey, $grey);


imagefilledrectangle($im,0,0,$imgwidth,$imgheight,$white);
imagefilledrectangle($im,15,15,$imgwidth-15,$imgheight-15,$grey);
imagerectangle($im,1,1,$imgwidth-1,$imgheight-1,$black);


// create end

$y=0;
$x=20;
$jump=0;
$acc=0;
if($nowmax > $imgheight){
$bili=$imgheight/$nowmax;
}else{
$bili=1;
}

//imagesetstyle($im, $style);
//imageline($im, 0, $imgheight-$arrayx[0]*$bili, 100, $imgheight-$arrayx[0]*$bili, IMG_COLOR_STYLED);
imagestring($im,3,20, $imgheight-$arrayx[0]*$bili-6,"<-- Left, current place.",$blue);

for($counter=0;$counter<count($arrayx);$counter++){
        $y=$arrayx[$counter]*$bili;
        if($counter==0){$new_y=$y;}
        $acc++;
        if(($x-1)>0 && ($acc%2)==0){
                $x++;
                $new_y=$imgheight-$y;
                imageline( $im, $x-1, $oy ,$x ,$new_y , $red );
               // imageline( $im, $x-1, $oy ,$x ,$new_y , $red );
                $oy=$new_y;
        }
        if($arrayx[$counter]==$nowmax){
                imagestring($im, 5, $x , $new_y+5 ,$arrayx[$counter], $blue);
        }elseif($arrayx[$counter]==$nowmin){
                imagestring($im, 5, $x , $new_y ,$arrayx[$counter], $blue);
        }
}

//date_default_timezone_set('GMT+8');
$nowtime=time()+8*3600;
//$today = date("Y M j G:i:s ",$nowtime);
$today = date("Y M j G:i:s ");
imagestring($im, 3, 220, 227, "Now time: $today",$black);


imagestring($im, 3, 20, 247, "Current: $arrayx[0]", $red);
imagestring($im, 3, 20, 257, "The max in recent 24hr: $nowmax", $black);
imagestring($im, 3, 20, 267, "The min in recent 24hr: $nowmin", $blue);
imagepng($im);
imagedestroy($im);
?>
