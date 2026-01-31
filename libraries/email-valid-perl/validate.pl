#!/usr/bin/env perl
use strict;
use warnings;
use Email::Valid;

my $file = $ARGV[0] or die "Usage: validate.pl <addresslist.txt>\n";
open my $fh, '<', $file or die "Cannot open $file: $!\n";

while (my $line = <$fh>) {
    chomp $line;
    next if $line eq '';

    my $valid = Email::Valid->address($line);
    my $result = $valid ? "valid   " : "invalid ";
    print "$result$line\n";
}

close $fh;
