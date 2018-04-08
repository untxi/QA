#include <stdio.h>
#include <string.h>


int validarMatriz (FILE* matriz){

    if (matriz == NULL) {// comprueba que el archivo exista
        return -1;
    }

    return 0;
}



void cargaMatriz (){

    FILE* matriz = NULL; // puntero para la matriz
    char* archivo = "PruebasGrupo07.txt"; // cargo el archivo
    char lectura [80]; // inicio de arreglo
    int numeroEntrada;
    int linea;
    int llave = 1;
    int largoLinea;
    int dimension;

    matriz = fopen(archivo, "r"); // abro el archivo en matriz
    validarMatriz(matriz);


    do{
    fscanf( matriz, " %[^\n] ", &lectura); // uso a lectura para que tome el valor de la linea
    printf("\n lectura: %s\n", lectura);
    largoLinea= strlen(lectura);
    printf("\n largo de la linea es %d\n", largoLinea);
    printf("\n lectura %s", lectura);
    //dimension = atoi(lectura);


    if (largoLinea == 1){
        dimension = atoi(lectura);
        linea = dimension;
        //dimensionMatriz(dimension, largoLinea, lectura);
        //printf("\n dimension %d \n", dimension);
    }

    if (largoLinea > 1){
        numeroEntrada = atoi(lectura);

        printf("\nlinea en formato numero %d\n", numeroEntrada);

        transformarArreglo (numeroEntrada, linea, largoLinea);

    }


    }while (dimension !=0);

}


void transformarArreglo (int linea, int dimension, int largoLinea){ // funcion que transforma el arreglo en la matriz para proceder a imprimirla

    int tmp, tmp2;
    int j=1;
    char caracterFila, caracterColumna;
    int temporal, entero;
    int array[largoLinea];

    int matrizdesordenada[dimension][dimension];

    char texto[largoLinea];

    itoa (linea, texto, 10);

    // for que permite llenar la matriz con unos
    for (int i=0; i<=dimension; i++){
        for (int j=0; j<=dimension; j++){
            matrizdesordenada[i][j]=1;
        }
    }

    // determina las coordenadas que entran del archivo para armar la matriz con 0

    for (int i=0; i<=dimension; i++){
        caracterFila = texto[i];
        i++;
        caracterColumna = texto[j];
        j= j+2;
        tmp = caracterFila - '0';
        tmp2 = caracterColumna - '0';
        matrizdesordenada [tmp][tmp2] = 0;
        //printf("\n linea en formato texto %c, ", texto[i]);
        //printf("\n linea en formato caracterFila %c, ", caracterFila);
        //printf("\n linea en fila numero %d, ", tmp);
        //printf("\n linea en columna numero %d, ", tmp2);
        //printf("\n| %d |");
        //printf("\n| %d |");
        //matrizdesordenada [tmp][tmp2] = 0;
    }


    for (int i=1; i<=dimension; i++){
        for (int j=1; j<=dimension; j++){
                  printf("| %d |",matrizdesordenada[i][j]);
        }
        printf("\n");

    }
    dimension=0;
    tmp2 = 0;
    tmp = 0;

    for (int i = 0 ; i<largoLinea; i++){
        temporal = texto[i];
        entero = temporal-'0';
        array[i] = entero;
       // printf("\n array %d", array[i]);
    }

    getmin_c (array, largoLinea);
}


// code gerardo **************************************************************************************

int getdif(int a, int b)
{
	int res = 0;


	if (a < b)
	{
		while (a < b)
		{
			res++;
			a++;
		}
		return res;
	}
	if (b < a)
	{
		while(b < a)
		{
			res++;
			b++;
		}
		return res;

	}
	else
		return res;

}

//Función para obtener la columna donde se harian menos movimientos.

void getmin_c(int arreglo [], int n)     // [ f, c ] -> [ i , i+1 ]
{
	int col_resultado = 0;
	int fil_resultado = 0;
	int dif = 0;
	int menor = n;
	int i;
	int j;

	for (i = 0; i < n; i = i + 2)
    {
        printf("Trabajando en ficha: %d , %d\n", arreglo[i], arreglo[i + 1]);
        for (j = 0; j < n; j = j + 2)
        {

			dif += getdif(arreglo[i+1],arreglo[j+1]);
			printf(" %d ->", dif);


		}
		//menor = dif;
		printf(" \n");

		printf("Diferencia encontrada con la columna %d es: %d \n", arreglo[i+1],dif);
		printf("El menor antes es: %i\n",menor);

		if (menor >= dif)
        {
        	menor = dif;
        	col_resultado = arreglo[i+1];
        	fil_resultado = arreglo[i];
        	dif = 0;
        	printf("El menor es: %d\n", menor);
        }
        else
        	dif = 0;
    }

    printf("El punto donde es menor la diferencia es en f: %d , c: %d \n", fil_resultado, col_resultado);
    return col_resultado;

}

//La funcion para obntener la fila para alinear en menos movimientos.

int getmin_f(int arreglo [], int n)     // [ f, c ] -> [ i , i+1 ]
{
	int col_resultado = 0;
	int fil_resultado = 0;
	int dif = 0;
	int menor = n;
	int i;
	int j;

	for (i = 0; i < n; i = i + 2)
    {
        printf("Trabajando en ficha: %d , %d\n", arreglo[i], arreglo[i + 1]);
        for (j = 0; j < n; j = j + 2)
        {

			dif += getdif(arreglo[i],arreglo[j]);
			printf(" %d ->", dif);


		}
		//menor = dif;
		printf(" \n");

		printf("Diferencia encontrada con la fila %d es: %d \n", arreglo[i],dif);
		printf("El menor antes es: %i\n",menor);

		if (menor >= dif)
        {
        	menor = dif;
        	col_resultado = arreglo[i+1];
        	fil_resultado = arreglo[i];
        	dif = 0;
        	printf("El menor es: %d\n", menor);
        }
        else
        	dif = 0;
    }

    printf("El punto donde es menor la diferencia es en  f: %d , c: %d \n", fil_resultado, col_resultado);
    return fil_resultado;

}//code Gerardo**************************************************************************************************



int main (){

    cargaMatriz();

    return 0;
}


