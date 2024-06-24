// Dia 9
// Ordenamiento de un Array: Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++! :)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    vector<int> array = {5,7,3,9,8,1};

    cout << "Números desordenados: ";
    for (int num : array) {
        cout << num << " ";
    }

    cout << endl;

    sort(array.begin(), array.end());

    cout << "numeros ordenados: ";

    for(int num : array) {
        cout << num << " ";
    }


    return 0;
}
