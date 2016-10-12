#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

$last_guess;
$min = 1;
$max = 100;

sub get_middle{
    my ($min, $max) = @_;
    return ($max + $min)//2;
}

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>A Guessing Game Player</title>
</head>
<body>
eof

warningsToBrowser(1);

$last_guess = param('last_guess');
$min = param('min');
$max = param('max');

$game_over = 0;

if (defined $last_guess) {
    if(defined param("higher")){
        $min = param('last_guess');
        $max = param('max');
    }elsif(defined param("lower")){
        $min = param('min');
        $max = param('last_guess');
    }else{
        $game_over = 1;
    }
}
if ($game_over){
    print "I win!\n";
print <<eof;
<form method="post" action="">
<input type="submit" value="Play Again">
</form>
eof
}else{
    $last_guess = get_middle($min,$max);
    print "My guess is:$last_guess\n";
    print <<eof;
    <form method="post" action="">
        <input type=hidden name="last_guess" value="$last_guess">
        <input type=hidden name="min" value="$min">
        <input type=hidden name="max" value="$max">
        <input type="submit" name="higher" value="Higher?">
        <input type="submit" name="correct" value="Correct?">
        <input type="submit" name="lower" value="Lower?">
    </form>
eof
}

print <<eof;
</body>
</html>
eof
