#!/usr/bin/perl -w
# validate a credit card number by calculating its
# checksum using Luhn's formula (https://en.wikipedia.org/wiki/Luhn_algorithm)

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html("Credit Card Validation"), "\n";
warningsToBrowser(1);
$credit_card = param("credit_card");
if (defined $credit_card) {
    print validate($credit_card);
}
print end_html;
exit 0;


sub luhn_checksum{
	my ($no) = @_;
	my $checksum = 0;
	my @digits = reverse(split //, $no);
	foreach $index (0..$#digits){
		$multipliter = 1 + $index % 2;
		$digit = $digits[$index] * $multipliter;
		if ($digit > 9){
			$digit -= 9;
		}
		$checksum += $digit;
	}
	return $checksum;
}

sub validate{
	my ($credit_no) = @_;
	my $no = $credit_no;
	$no =~ s/\D//g;
	if(length $no != 16){
		return "$credit_no is invalid - does not contain exactly 16 digits\n";
	}elsif(luhn_checksum($no) % 10 == 0){
		return "$credit_no is valid\n";
	}else{
		return "$credit_no is invalid\n";
	}	
}

