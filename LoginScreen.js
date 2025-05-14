import React, { useState } from "react";
import { View, Text, TextInput, Button } from "react-native";

export default function LoginScreen({ navigation }) {
  const [userId, setUserId] = useState("");

  const handleLogin = () => {
    navigation.navigate("Home", { userId });
  };

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "white",
      }}
    >
      <Text style={{ fontSize: 24, color: "blue" }}>Login</Text>
      <TextInput
        placeholder="ID do usuário"
        onChangeText={setUserId}
        keyboardType="numeric"
        style={{ borderWidth: 1, width: 200, marginBottom: 10 }}
      />
      <Button title="Entrar" onPress={handleLogin} color="black" />
    </View>
  );
}
