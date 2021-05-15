#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE *fcollected_data;
	fcollected_data = fopen("sum_values.txt", "r");
	
	int sum = 0;
	int *values;
	values = (int*)malloc(50*sizeof(int));

	if(fcollected_data == NULL){	
		printf("Error! Data could not be found");
		exit(1);
	}
	else{
		while(fscanf(fcollected_data, "%d", values) != EOF){
			sum += *values;
		}
	}

	printf("The result is %d\n", sum);

	fclose(fcollected_data);

	fcollected_data = fopen("final_sum.txt", "w+");

	fprintf(fcollected_data, "%d\n", sum);

	fclose(fcollected_data);

	return 0;

}



