#!/bin/sh
echo content-type:text/html
echo

env_var=`env`

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>show_environment_variables.sh.cgi</title>
</head>
<body>
<h2>Environment Variables</h2>
<pre>
echo $env
</pre>
</body>
</html>
eof
