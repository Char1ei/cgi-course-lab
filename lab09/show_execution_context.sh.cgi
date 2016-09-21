#!/bin/sh
echo content-type:text/html
echo

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>show_execution_context.sh.cgi</title>
</head>
<body>
<h2>Execution Environment</h2>
<pre>
eof

for command in pwd id hostname 'uname -a'
do 
	echo "$command: `$command`"
done

cat <<eof
</pre>
</body>
</html>
eof
