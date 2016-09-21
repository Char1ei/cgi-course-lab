#!/bin/sh
echo content-type:text/html
echo

if [ "$REQUEST_METHOD" = "GET" ]
then
	# echo GET 
	parameters=$QUERY_STRING
else
	# echo POST
	read parameters # read a line from stdin
fi

# parameters='x=1&y=2'
x=`echo $parameters | sed '
	s/.*x=//
	s/&.*//
	s/[^0-9\-\.\+]//gi
	'`
# echo $x
y=`echo $parameters | sed '
	s/.*y=//
	s/&.*//
	s/[^0-9\-\.\+]//g
	'`
sum='?'
test "$x" -a "$y" && sum=`expr "$x" '+' "$y"` # -a is logic and
# echo $sum

cat <<eof #cat until eof
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>sum toe numbers</title>
	</head>
	<body>
eof

cat <<eof
	<form method = "POST" action="">
		<input type = "textfield" name = "x" value ="$x">
		+
		<input type = "textfield" name = "y" value = "$y">
		=
		$sum
		<input type = "submit" value = "calculate">
	</form>
	</body>
</html>
eof
