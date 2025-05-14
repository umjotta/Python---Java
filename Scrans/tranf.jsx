import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
} from "react-native";

const TransferScreen = () => {
  const [amount, setAmount] = useState("0,00");
  const balance = "10,00";

  const handlePress = (value) => {
    if (value === "C") {
      setAmount("0,00");
    } else {
      setAmount((prev) => (prev === "0,00" ? value : prev + value));
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.label}>Qual é o valor da transferência?</Text>
      <Text style={styles.balance}>Saldo: R$ {balance}</Text>
      <TextInput style={styles.input} value={`R$ ${amount}`} editable={false} />

      <View style={styles.keyboard}>
        {["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "C"].map(
          (item) => (
            <TouchableOpacity
              key={item}
              style={styles.key}
              onPress={() => handlePress(item)}
            >
              <Text style={styles.keyText}>{item}</Text>
            </TouchableOpacity>
          )
        )}
      </View>

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Enviar</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center", justifyContent: "center" },
  label: { fontSize: 18, fontWeight: "bold" },
  balance: { fontSize: 16, marginVertical: 5 },
  input: { fontSize: 24, fontWeight: "bold", marginBottom: 10 },
  keyboard: {
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "center",
  },
  key: {
    width: 50,
    height: 50,
    justifyContent: "center",
    alignItems: "center",
    margin: 5,
    backgroundColor: "#ddd",
  },
  keyText: { fontSize: 20 },
  button: {
    marginTop: 20,
    backgroundColor: "green",
    padding: 10,
    borderRadius: 5,
  },
  buttonText: { color: "white", fontWeight: "bold" },
});

export default TransferScreen;
