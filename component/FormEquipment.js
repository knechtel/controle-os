import React, { useState } from "react";
import { useEffect } from "react";
import {
  View,
  TextInput,
  Button,
  Text,
  Alert,
  StyleSheet,
  ScrollView,
} from "react-native";
import { Checkbox } from "react-native-paper";
import { FIND_BY_ID_CLIENT, UPDATE_EQUIPMENT } from "../util/urls";

const FormEquipment = ({ route, navigation }) => {
  const [id, setId] = useState();
  const [entregue, setEntregue] = useState(false);
  const [garantia, setGarantia] = useState(false);
  const [descricao, setDescricao] = useState("");
  const [modelo, setModelo] = useState("");
  const [serial, setSerial] = useState("");
  const [marca, setMarca] = useState("");
  const [defeito, setDefeito] = useState("");
  const [preco, setPreco] = useState("");
  // useEffect será executado quando o componente for montado
  useEffect(() => {
    idClient = route.params.paramKey;

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
        setDescricao(json["equipments"][0].description);
        setGarantia(json["equipments"][0].garantia);
        setEntregue(json["equipments"][0].entregue);
        setModelo(json["equipments"][0].model);
        setSerial(json["equipments"][0].serial);
        setMarca(json["equipments"][0].brand);
        setDefeito(json["equipments"][0]["defectDefectForRepair"]);
        setPreco(String(json["equipments"][0]["price"]) + ".00");
        setId(json["equipments"][0].id);
        console.log("id  = " + id);
      });
    
    return () => {
      console.log("Componente desmontado!");
    };
  }, []); 
  
  
  const handleSubmit = () => {
    fetch(UPDATE_EQUIPMENT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id: id,
        description: descricao,
        model: modelo,
        serial: serial,
        brand: marca,
        defectForRepair: defeito,
        price: parseFloat(preco),
        entregue: entregue,
        garantia: garantia,
      }),
    })
      .then((response) => response.json())
      .then((json) => {});
    alert("Equipamento editado com sucesso!");
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Formulário de Equipamento</Text>

      <TextInput
        style={styles.input}
        placeholder="Descrição"
        value={descricao}
        onChangeText={setDescricao}
      />

      <TextInput
        style={styles.input}
        placeholder="Modelo"
        value={modelo}
        onChangeText={setModelo}
      />

      <TextInput
        style={styles.input}
        placeholder="Serial"
        value={serial}
        onChangeText={setSerial}
      />

      <TextInput
        style={styles.input}
        placeholder="Marca"
        value={marca}
        onChangeText={setMarca}
      />

      <TextInput
        style={styles.input}
        placeholder="Defeito"
        value={defeito}
        onChangeText={setDefeito}
      />

      <TextInput
        style={styles.input}
        placeholder="Preço"
        value={preco}
        onChangeText={(preco) => setPreco(preco)}
        keyboardType="numeric"
      />

      <View style={{ padding: 10 }}>
        <Checkbox
          status={entregue ? "checked" : "unchecked"}
          onPress={() => {
            setEntregue(!entregue);
          }}
        />
        <Text>Entregue</Text>
      </View>
      <View style={{ padding: 10 }}>
        <Checkbox
          status={garantia ? "checked" : "unchecked"}
          onPress={() => {
            setGarantia(!garantia);
          }}
        />
        <Text>Garantia</Text>
      </View>
      <Button title="Enviar" onPress={handleSubmit} />
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    flexGrow: 1,
    justifyContent: "center",
    justifyContent: "space-between",
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

export default FormEquipment;
