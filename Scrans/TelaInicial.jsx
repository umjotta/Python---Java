import React from "react";
import { View, Text, Button, StyleSheet } from "react-native";

const CurrencyConverterScreen = () => {
  return (
    <View style={styles.container}>
      <View style={styles.profileContainer}>
        <Text style={styles.userName}>Aluno</Text>
        <Text style={styles.userTag}>#6#9e34</Text>
      </View>

      <View style={styles.card}>
        <Text style={styles.label}>Money</Text>
        <Text style={styles.value}>259</Text>
        <Text style={styles.percentage}>Conversão: 10%</Text>
      </View>

      <View style={styles.card}>
        <Text style={styles.label}>Coins</Text>
        <Text style={styles.value}>$250</Text>
        <Text style={styles.percentage}>Conversão: 100%</Text>
      </View>

      <Button
        title="Enviar para um banco"
        onPress={() => console.log("Enviado para o banco")}
      />

      <View style={styles.marketContainer}>
        <Text style={styles.label}>Bolsa</Text>
        {/* Aqui você pode adicionar um gráfico usando bibliotecas como react-native-chart-kit */}
      </View>

      <Button
        title="Fazer a conversão"
        onPress={() => console.log("Conversão realizada")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: "#fff" },
  profileContainer: { alignItems: "center", marginBottom: 20 },
  userName: { fontSize: 20, fontWeight: "bold" },
  userTag: { fontSize: 16, color: "gray" },
  card: {
    padding: 15,
    backgroundColor: "#e3e3e3",
    marginVertical: 10,
    borderRadius: 10,
  },
  label: { fontSize: 16, fontWeight: "bold" },
  value: { fontSize: 18, color: "#333" },
  percentage: { fontSize: 14, color: "gray" },
  marketContainer: {
    padding: 15,
    backgroundColor: "#f5f5f5",
    borderRadius: 10,
    marginTop: 20,
  },
});

export default CurrencyConverterScreen;
