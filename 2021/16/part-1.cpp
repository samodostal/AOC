#include "../lib/template.cpp"

string hexadecimal_to_binary(string hexadecimal) {
  string binary = "";
  FOR(i, hexadecimal) {
    char c = hexadecimal[i];
    int num = ((c >= 'A') ? (c - 'A' + 10) : (c - '0'));
    string bin = bitset<4>(num).to_string();
    binary += bin;
  }
  return binary;
}

int binary_to_decimal(string binary) {
  int decimal = 0;
  FOR(i, binary) {
    decimal += (binary[i] - '0') * pow(2, binary.length() - i - 1);
  }
  return decimal;
}

string packet(string binary, int &result) {
  int packet_version = binary_to_decimal(binary.substr(0, 3));
  int packet_type_id = binary_to_decimal(binary.substr(3, 3));
  string binary_rest = binary.substr(6);

  result += packet_version;

  if (packet_type_id == 4) { // Literal value packet
    cout << "Literal packet | V: " << packet_version << " | T: " << packet_type_id << endl;
    cout << binary << endl;

    string binary_number = "";
    while(true) {
      string binary_group = binary_rest.substr(0, 5);
      binary_rest = binary_rest.substr(5);

      binary_number += binary_group.substr(1);

      if(binary_group[0] == '0') break;
    }
    cout << "Binary number: " << binary_to_decimal(binary_number) << endl;
    cout << endl;
    return binary_rest;
  } else { // Operator packet
    cout << "Operator packet | V: " << packet_version << " | T: " << packet_type_id << endl;
    cout << binary << endl << endl;

    char length_type_id = binary_rest[0];
    binary_rest = binary_rest.substr(1);

    if (length_type_id == '0'){
      int total_length = binary_to_decimal(binary_rest.substr(0, 15));
      binary_rest = binary_rest.substr(15);
      int literal_length = 0;

      while(true) {
        string rest  = packet(binary_rest, result);
        literal_length += binary_rest.length() - rest.length();
        binary_rest = rest;

        if(literal_length >= total_length) break;
      }

      cout << binary_rest << endl;
    } else {
      int subpackets_length = binary_to_decimal(binary_rest.substr(0, 11));
      binary_rest = binary_rest.substr(11);

      while(subpackets_length--) {
        binary_rest = packet(binary_rest, result);
      }
    }
    return binary_rest;
  }
}

int main() {
  f file("16/set.txt");

  string hexadecimal, binary;
  file >> hexadecimal;
  binary = hexadecimal_to_binary(hexadecimal);

  int result = 0;
  packet(binary, result);

  cout << "Result: " << result << endl;
}
