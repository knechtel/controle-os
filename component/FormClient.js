import { useEffect } from "react";
import React, { useState } from "react";
import {
  TouchableOpacity,
  View,
  TextInput,
  Button,
  Alert,
  StyleSheet,
  ScrollView,
  Text,
} from "react-native";
import { FIND_BY_ID_CLIENT, UPDATE_CLIENT } from "../util/urls";
redirectToEdit = (id) => {
  navigation.navigate("Equipment", { paramKey: id });
};
const FormClient = ({ route, navigation }) => {
  const [nome, setNome] = useState("");
  const [id, setId] = useState("");
  const [cpf, setCpf] = useState("");
  const [telefone, setTelefone] = useState("");
  const [email, setEmail] = useState("");
  const [endereco, setEndereco] = useState("");
  redirectToEdit = () => {
    navigation.navigate("Equipment", { paramKey: id });
  };
  useEffect(() => {
    idClient = route.params.paramKey;
    setId(idClient);
    fetch(FIND_BY_ID_CLIENT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id: idClient,
      }),
    })
      .then((response) => response.json())
      .then((json) => {
        setEmail(json["email"]);
        setNome(json["name"]);
        setEndereco(json["address"]);
        setCpf(json["cpf"]);
        setTelefone(json["phone"]);
      });
    return () => {
      console.log("Componente desmontado!");
    };
  }, []);
  const handleSubmit = () => {
    fetch(UPDATE_CLIENT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id: id,
        name: nome,
        address: endereco,
        cpf: String(cpf),
        phone: telefone,
        email: email,
      }),
    })
      .then((response) => response.json())
      .then((json) => {
        setEmail(json["email"]);
        setNome(json["name"]);
        setEndereco(json["address"]);
        setCpf(json["cpf"]);
        setTelefone(json["phone"]);
      });
    alert("Cliente editado com sucesso!");
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Formulário de Cliente</Text>
      <TextInput
        style={styles.input}
        placeholder="Nome"
        value={nome}
        onChangeText={setNome}
      />

      <TextInput
        style={styles.input}
        placeholder="CPF"
        value={cpf}
        onChangeText={setCpf}
        keyboardType="numeric"
        maxLength={15} // Limita o número de caracteres do CPF a 11
      />

      <TextInput
        style={styles.input}
        placeholder="Telefone"
        value={telefone}
        onChangeText={setTelefone}
        keyboardType="phone-pad"
      />

      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
      />

      <TextInput
        style={styles.input}
        placeholder="Endereço"
        value={endereco}
        onChangeText={setEndereco}
      />
      <Button title="Enviar" onPress={handleSubmit} />
      <View style={stylesLink.container}>
        <Text>Detalhes do Equipamento!</Text>
        <TouchableOpacity onPress={redirectToEdit}>
          <Text style={stylesLink.link}>Clique aqui</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: "center",
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 20,
  },
  input: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
});
const stylesLink = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  link: {
    color: "blue",
    textDecorationLine: "underline",
  },
});
export default FormClient;
