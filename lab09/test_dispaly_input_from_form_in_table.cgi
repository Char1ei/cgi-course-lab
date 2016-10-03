#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Input Parameters</h2>
<hr>
<table border=1>
";

if ($ENV{REQUEST_METHOD} eq 'POST') {
    $parameters = <>;
} else {
    $parameters = $ENV{QUERY_STRING}
}

foreach (split(/\&/, $parameters)) {
    /([^=]*)=(.*)/;
    print "<tr><td>$1<td>$2\n";
}


print "
</table>
<hr>
</body>
</html>
";
