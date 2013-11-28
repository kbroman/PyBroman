#!/usr/bin/perl
#
# Combine the data in "genotypes.txt", "markers.txt" and "families.txt" 
# and convert into a CRI-MAP .gen file.

# file names
$gfile = "genotypes.txt";  # genotype data
$mfile = "markers.txt";    # list of markers, in order
$ffile = "families.txt";   # family information 
$ofile = "data.gen";       # output file

# read marker names and place in the vector @markers
open(IN, $mfile) or die("Cannot read from $mfile");
while($line = <IN>) {
    chomp($line);
    push(@markers, $line);
}
close(IN);

# read family information and place in the hashes %dad, %mom, %sex
open(IN, $ffile) or die("Cannot read from $ffile");
$line = <IN>;
while($line = <IN>) {
    chomp($line);
    @v = split(/\s+/, $line);
    if($v[0] eq "") { shift @v; }
    
    ($fam, $ind, $dad, $mom, $sex) = @v;
    
    $dad{$fam}{$ind} = $dad;
    $mom{$fam}{$ind} = $mom;

    if($sex == 2) {   # make female = 0 rather than = 2 
	$sex{$fam}{$ind} = 0;
    }
    else {  
	$sex{$fam}{$ind} = $sex;
    }
}
close(IN);

# read genotype data
open(IN, $gfile) or die("Cannot read from $gfile");

# header line : parse family/individual IDs
$line = <IN>; chomp($line);
@v = split(/\s+/, $line);
if($v[0] eq "") { shift @v; } # if first entry is blank, get rid of it
shift @v; # get rid of the first entry "Marker"
foreach $v (@v) {
    ($fam,$ind) = split(/-/, $v); # split at '-'
    @fam = (@fam, $fam);
    @ind = (@ind, $ind);
}

# parse rest of file 
while($line = <IN>) {

    $marker = substr($line, 0, 9);
    $marker =~ s/\s+//g; # remove any extra spaces
    
    foreach $i (0..(@fam-1)) {
	$g = substr($line, 9+$i*7, 7); 
	($g1, $g2) = split(/\//, $g);  # split at '/'
	$g1 =~ s/\s+//g; # remove any extra spaces
	$g2 =~ s/\s+//g;

	if($g1 == 0 or $g2 == 0) { # replace blanks with 0's
	    $g1 = 0;
	    $g2 = 0;
	}

	$gen{$fam[$i]}{$ind[$i]}{$marker} = $g1 . " " . $g2;
	
    }
}
close(IN);


# write genotype data as cri-map .gen file
open(OUT, ">$ofile") or die("Cannot write to $ofile");

$nfam = keys %gen;      # number of families
print OUT ("$nfam\n");
$nmar = @markers;       # number of markers
print OUT ("$nmar\n");
foreach $mar (@markers) {
    print OUT ("$mar\n");
}

foreach $fam (sort numerically keys %gen) {  # families in numerical order
    print OUT ("$fam\n");
    $nind = keys %{$gen{$fam}};  # number of individuals in family
    print OUT ("$nind\n");

    foreach $ind (sort numerically keys %{$gen{$fam}}) {
	print OUT ("$ind $mom{$fam}{$ind} $dad{$fam}{$ind} $sex{$fam}{$ind}\n");
	
	foreach $mar (@markers) {  # markers in order
	    print OUT ("$gen{$fam}{$ind}{$mar} ");
	}

	print OUT ("\n");
    }
}
close(OUT);


# subroutine to allow sorts by numerical order
sub numerically { $a <=> $b; }
