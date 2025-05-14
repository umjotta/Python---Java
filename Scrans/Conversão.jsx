import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";

const ConversionScreen = () => {
  const [coins, setCoins] = useState("");
  const exchangeRate = 0.066; // Exemplo: 1 Coin = 0.066 Reais

  const handleConversion = () => {
    const reais = parseFloat(coins) * exchangeRate;
    alert(`Valor em Reais: R$ ${reais.toFixed(2)}`);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>CoinVert</Text>

      <View style={styles.inputContainer}>
        <Text style={styles.label}>Coins</Text>
        <TextInput
          style={styles.input}
          keyboardType="numeric"
          value={coins}
          onChangeText={setCoins}
          placeholder="Digite o valor em Coins"
        />
      </View>

      <Text style={styles.convertedValue}>
        R$ {(parseFloat(coins) * exchangeRate).toFixed(2) || "0.00"}
      </Text>

      <Button title="Converter" onPress={handleConversion} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#fff",
  },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
  inputContainer: { marginBottom: 10, alignItems: "center" },
  label: { fontSize: 18, fontWeight: "bold" },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    padding: 10,
    width: "80%",
    fontSize: 18,
    textAlign: "center",
    marginTop: 5,
  },
  convertedValue: { fontSize: 20, fontWeight: "bold", marginVertical: 15 },
});

export default ConversionScreen;
