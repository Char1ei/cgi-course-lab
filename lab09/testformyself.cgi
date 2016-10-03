#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html('Login');
warningsToBrowser(1);

if ( my $name = param('name') ) {
    print "Your name is $name.<br />";
}

if ( my $age = param('age') ) {
    print "You are $age years old.";
}

print end_html;
