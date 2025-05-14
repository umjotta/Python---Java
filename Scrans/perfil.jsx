import React, { useState } from "react";
import { View, Text, Button, Modal, StyleSheet } from "react-native";

const ProfileScreen = () => {
  const [modalVisible, setModalVisible] = useState(false);

  return (
    <View style={styles.container}>
      <Button title="Abrir Perfil" onPress={() => setModalVisible(true)} />

      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalContainer}>
          <View style={styles.profileCard}>
            <Text style={styles.name}>Nome: Aluno</Text>
            <Text style={styles.tag}>Tag: 6#9e34</Text>
            <Text style={styles.school}>
              Escola: ETE Porto Digital, Rec - PE, 2025
            </Text>
            <Button
              title="Sair"
              color="red"
              onPress={() => setModalVisible(false)}
            />
          </View>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", alignItems: "center" },
  modalContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0,0,0,0.8)",
  },
  profileCard: {
    padding: 20,
    backgroundColor: "#222",
    borderRadius: 10,
    alignItems: "center",
  },
  name: { fontSize: 20, color: "#fff", fontWeight: "bold" },
  tag: { fontSize: 16, color: "#ccc" },
  school: { fontSize: 14, color: "#bbb", marginBottom: 20 },
});

export default ProfileScreen;
