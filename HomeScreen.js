import React, { useState, useEffect } from "react";
import { View, Text } from "react-native";
import axios from "axios";

export default function HomeScreen({ route }) {
  const [usuario, setUsuario] = useState(null);
  const { userId } = route.params;

  useEffect(() => {
    axios
      .get(`http://localhost:3000/usuario/${userId}`)
      .then((response) => setUsuario(response.data))
      .catch(() => alert("Usuário não encontrado"));
  }, []);

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "white",
      }}
    >
      {usuario ? (
        <>
          <Text style={{ fontSize: 24, color: "blue" }}>
            Olá, {usuario.nome}!
          </Text>
          <Text style={{ fontSize: 20, color: "black" }}>
            Saldo de SCoins: {usuario.scoins}
          </Text>
          <Text style={{ fontSize: 20, color: "black" }}>
            Valor em R$: {(usuario.scoins * 0.1).toFixed(2)}
          </Text>
        </>
      ) : (
        <Text style={{ fontSize: 20, color: "red" }}>Carregando...</Text>
      )}
    </View>
  );
}
