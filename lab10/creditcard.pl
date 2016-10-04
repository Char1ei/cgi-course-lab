#!/usr/bin/perl -w
# validate a credit card number by calculating its
# checksum using Luhn's formula (https://en.wikipedia.org/wiki/Luhn_algorithm)

sub luhn_checksun{
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
	my ($no) = @_;
	$no =~ s/\D//g;
	if(length $no != 16){
		return "invalid - does not contain exactly 16 digits\n";
	}elsif(luhn_checksum($no) $ 10 == 0){
		return "valid\n";
	}else{
		return "invalid\n";
	}	
}

foreach $credit_no (@ARGV){
	print "$credit_no is validate($credit_no)\n";
}
