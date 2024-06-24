// Dia 10
// Palíndromo: Escribir un programa que determine si una cadena de caracteres ingresada por el usuario es un palíndromo ¡Pero hazlo en C++! :)

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string p_usuario, p_invertida;

    cout << "Ingrese una palabra: ";
    cin >> p_usuario;

    p_invertida = p_usuario; // Copiamos la palabra original a p_invertida

    // Invertir la cadena utilizando std::reverse
    reverse(p_invertida.begin(), p_invertida.end());

    cout << "Palabra invertida: " << p_invertida << endl;

    // Verificar si es un palíndromo
    if (p_usuario == p_invertida) {
        cout << "Es una palabra palíndromo." << endl;
    } else {
        cout << "No es una palabra palíndromo." << endl;
    }

    return 0;
}
