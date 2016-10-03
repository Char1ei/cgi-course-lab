#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# The value entered last time is made the initial value
# of the text field

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Initializing A Form');
warningsToBrowser(1);

$last_value = param("string");
if (defined $last_value) {
    print "Last time you entered: $last_value \n";
print "<p>\n";
    param("string", ""); # clear the field
	print "hidden var = ",param("h"),"\n";
} else {
    param("string", "initial value");
}

print start_form, "\n";
print "Enter a string: \n";
print textfield('string'), "\n";
print hidden(-name => "h", -value => "valueofhivar"), "\n";
print end_form, "\n";
print end_html, "\n";
