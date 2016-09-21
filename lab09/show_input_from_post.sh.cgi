#!/bin/sh
echo content-type:text/html
echo

# env=`env`

read input

input=`echo $input|sed s/.*=//`

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>show_environment_variables.sh.cgi</title>
</head>
<body>
# echo $env
<h2>Environment Variables</h2>
<pre>
<form method = "POST" action="">
		<input type = "textfield" name = "input" value = "$input">
		<input type ="submit" value = "submit">
	</form>
<p>
echo "input: $input"
</pre>
</body>
</html>
eof
