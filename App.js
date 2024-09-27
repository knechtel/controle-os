import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  Button,
  Alert,
  StyleSheet,
  Image,
  Dimensions,
} from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import ClientList from "./component/ClientList";
import FormEquipment from "./component/FormEquipment";
import FormClient from "./component/FormClient";
import { FIND_USER } from "./util/urls";
const { width: SCREEN_WIDTH, height: SCREEN_HEIGHT } = Dimensions.get("window");
const Login = ({ navigation }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    if (username === "admin" && password === "1234") {
      fetch(FIND_USER, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          login: "maiquel",
          password: "123",
        }),
      })
        .then((response) => response.json())
        .then((json) => {});

      navigation.navigate("Client");
    } else {
      Alert.alert("Erro", "Usuário ou senha inválidos");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Eletrônica São José </Text>
      <Image
        source={require("./assets/eletronicaLogo.png")} // Substitua pela URL da sua imagem ou use require para imagens locais
        style={styles.headerImage} // Estilo da imagem
      />
      <TextInput
        style={styles.input}
        placeholder="Usuário"
        value={username}
        onChangeText={setUsername}
      />

      <TextInput
        style={styles.input}
        placeholder="Senha"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />

      <Button title="Entrar" onPress={handleLogin} />
    </View>
  );
};
// Criando o Stack Navigator
const Stack = createStackNavigator();
const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Login} />
        <Stack.Screen name="Client" component={ClientList} />
        <Stack.Screen name="Equipment" component={FormEquipment} />
        <Stack.Screen name="FormClient" component={FormClient} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
  },
  headerImage: {
    width: SCREEN_WIDTH * 0.9, // Largura da imagem
    height: SCREEN_HEIGHT * 0.3, // Altura da imagem
    //  borderRadius: 25, // Deixa a imagem redonda, caso seja quadrada
    marginBottom: 10, // Espaço entre a imagem e o texto
    //  marginHorizontal: SCREEN_WIDTH * 0.1,
    alignItems: "center",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  input: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});
export default App;
