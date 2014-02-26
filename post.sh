#! /bin/bash
nltr=$(wc -l tree | cut -d ' ' -f 1)
nlph=$(wc -l path | cut -d ' ' -f 1)
echo  "nlines of file 'tree' is : "$nltr
echo  "nlines of file 'path' is : "$nlph
reg_arti="[0-9]{4}-[0-9]{2}-[0-9]{2}"
declare -a path_arr

for((i=1; i<= nlph; i++)) {
	lipth=$(awk -v n=$i 'NR==n{print}' path);
	path_arr[$i]=$lipth;
}

for((i=1; i <= nlph; i++)) {
	echo "we need it"${path_arr[$i]};
}
index_path=1;
for((i=1; i <= nltr; i++)) {
	lines=$(awk -v n=$i 'NR==n{print}' tree);

	 awk -v li="$lines" -v reg="$reg_arti" -v  arr="$path_arr" -v index_path="$index_path" -v i="$i"  'BEGIN {  
		if(match(li, reg)) {
			printf("%s -->matched\n", li);

		} else {
			printf("%s --> unmatch\n",li);
		}

	}'   
}





