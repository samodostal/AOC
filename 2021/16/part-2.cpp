#include "../lib/template.cpp"
#include <utility>

string hexadecimal_to_binary(string hexadecimal) {
  string binary = "";
  FOR(i, hexadecimal) {
    char c = hexadecimal[i];
    long num = ((c >= 'A') ? (c - 'A' + 10) : (c - '0'));
    string bin = bitset<4>(num).to_string();
    binary += bin;
  }
  return binary;
}

long binary_to_decimal(string binary) {
  long decimal = 0;
  FOR(i, binary) {
    decimal += (binary[i] - '0') * pow(2, binary.length() - i - 1);
  }
  return decimal;
}

pair<string, long> packet(string binary) {
  long packet_version = binary_to_decimal(binary.substr(0, 3));
  long packet_type_id = binary_to_decimal(binary.substr(3, 3));
  string binary_rest = binary.substr(6);

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
    return make_pair(binary_rest, binary_to_decimal(binary_number));
  } else { // Operator packet
    cout << "Operator packet | V: " << packet_version << " | T: " << packet_type_id << endl;
    cout << binary << endl << endl;

    char length_type_id = binary_rest[0];
    binary_rest = binary_rest.substr(1);

    vector<long> package_values;

    if (length_type_id == '0'){
      long total_length = binary_to_decimal(binary_rest.substr(0, 15));
      binary_rest = binary_rest.substr(15);
      long literal_length = 0;

      while(true) {
        pair<string, long> res = packet(binary_rest);
        string rest = res.first;
        literal_length += binary_rest.length() - rest.length();
        binary_rest = rest;

        package_values.push_back(res.second);

        if(literal_length >= total_length) break;
      }

      cout << binary_rest << endl;
    } else {
      long subpackets_length = binary_to_decimal(binary_rest.substr(0, 11));
      binary_rest = binary_rest.substr(11);

      while(subpackets_length--) {
        pair<string, long> res = packet(binary_rest);
        binary_rest = res.first;

        package_values.push_back(res.second);
      }
    }

    long result;
    
    if(packet_type_id == 0) {
      result = 0;
      FOR(i, package_values) {
        result += package_values[i];
      }
    } else if (packet_type_id == 1) {
      result = 1;
      FOR(i, package_values) {
        result *= package_values[i];
      }
    } else if (packet_type_id == 2) {
      result = package_values[0];
      FOR(i, package_values) {
        if(package_values[i] < result) result = package_values[i];
      }
    } else if (packet_type_id == 3) {
      result = package_values[0];
      FOR(i, package_values) {
        if(package_values[i] > result) result = package_values[i];
      }
    } else if (packet_type_id == 5) {
      result = 0;
      if(package_values[0] > package_values[1]) result = 1;
    } else if (packet_type_id == 6) {
      result = 0;
      if(package_values[0] < package_values[1]) result = 1;
    } else if (packet_type_id == 7) {
      result = 0;
      if(package_values[0] == package_values[1]) result = 1;
    }

    return make_pair(binary_rest, result);
  }
}

int main() {
  f file("16/set.txt");

  string hexadecimal, binary;
  file >> hexadecimal;
  binary = hexadecimal_to_binary(hexadecimal);

  pair<string, long> result = packet(binary);

  cout << "Result: " << result.second << endl;
}
