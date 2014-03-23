
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>


#define MAXLEN  1024

int main (int argc, char *argv[])
{
	FILE *fp;
	char buf[MAXLEN];
	char *filename = argv[1];
	char *lines, errbuf[MAXLEN];
	int err;
	const char *pattern = "^.*[0-9]{4}-[0-9]{2}-[0-9]{2}-.*$";
	const size_t nmath = 1;
	regmatch_t pmatch[1];
	regex_t reg;
	if (!(fp = fopen(filename, "r")))
	  {
		printf ("Error when open file: %s\n", filename);
		exit (0);
	  }
	if (regcomp(&reg, pattern, REG_EXTENDED) < 0)
	  {
		regerror (err, &reg, errbuf, sizeof(errbuf));
		printf ("%s\n", errbuf);
	  }
	 while ((fgets (buf, MAXLEN, fp)) != NULL)
	   {
		lines = buf;
		err = regexec (&reg, lines, nmath, pmatch, 0);
		if (err == 0)
	 	  {
			printf ("------> %s\n", lines); 	
		  }

	   }
	regfree (&reg);
	return 0;



}





