import React, { useState } from 'react'
import { View, StyleSheet, TouchableOpacity } from 'react-native'
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Logo from '../components/Logo'
import Header from '../components/Header'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'
import { emailValidator } from '../helpers/emailValidator'
import { passwordValidator } from '../helpers/passwordValidator'
import { nameValidator } from '../helpers/nameValidator'
import { IDNumberValidator } from '../helpers/IDValidator'
import { cPasswordValidator } from '../helpers/cPAsswordValidator'



const submitToApi = async() =>{

  if(true){
    await fetch('http://127.0.0.1:8000/register-create/'),{
      method : 'POST',
      headers:{
        'Accept': 'application/json',
        'Content-type': 'application/json',
      },
      body: JSON.stringify({
        'name':name,
        'surname':surName,
        'email':email,
        'password':password,
        'cPasword':cPassword,
        'ID-number':ID_number,
        
      })
    }
  }
}



export default function RegisterScreen({ navigation }) {
  const [name, setName] = useState({ value: '', error: '' })
  const [surName, setsurName] = useState({ value: '', error: '' })
  const [email, setEmail] = useState({ value: '', error: '' })
  const [password, setPassword] = useState({ value: '', error: '' })
  const [cPassword, setcPassword] = useState({ value: '', error: '' })
  const [ID_number, setID_number] = useState({ value: '', error: '' })







  const onSignUpPressed = () => {
    const nameError = nameValidator(name.value)
    const surNameError = nameValidator(surName.value)
    const emailError = emailValidator(email.value)
    const passwordError = passwordValidator(password.value)
    const cPasswordError = cPasswordValidator(cPassword.value)
    const ID_numberError = IDNumberValidator(ID_number.value)
  

    if (emailError || passwordError || nameError || surNameError || ID_numberError || cPasswordError) {
      setName({ ...name, error: nameError })
      setEmail({ ...email, error: emailError })
      setPassword({ ...password, error: passwordError })
      setsurName({ ...surName, error: surNameError })
      setID_number({ ...ID_number, error: ID_numberError })
      setcPassword({ ...cPassword, error: cPasswordError })
      return 
    }
    navigation.reset({
      index: 0,
      routes: [{ name: 'Dashboard' }],

      
    })
 
  }

  return (
    
    <Background>
      <BackButton goBack={navigation.goBack} />
      <Logo />
      <Header>Create Account</Header>
      <TextInput
        label="Name"
        returnKeyType="next"
        value={name.value}
        onChangeText={(text) => setName({ value: text, error: '' })}
        error={!!name.error}
        errorText={name.error}
      />
      <TextInput
        label="Email"
        returnKeyType="next"
        value={email.value}
        onChangeText={(text) => setEmail({ value: text, error: '' })}
        error={!!email.error}
        errorText={email.error}
        autoCapitalize="none"
        autoCompleteType="email"
        textContentType="emailAddress"
        keyboardType="email-address"
      />
      <TextInput
        label="Password"
        returnKeyType="done"
        value={password.value}
        onChangeText={(text) => setPassword({ value: text, error: '' })}
        error={!!password.error}
        errorText={password.error}
        // secureTextEntry
      />
      <TextInput
        label="Confirm Password"
        returnKeyType="done"
        value={cPassword.value}
        onChangeText={(text) => setcPassword({ value: text, error: '' })}
        error={!!cPassword.error}
        errorText={cPassword.error}
        // secureTextEntry
      />
       <TextInput
        label="ID Number"
        returnKeyType="done"
        value={ID_number.value}
        onChangeText={(text) => setID_number({ value: text, error: '' })}
        error={!!ID_number.error}
        errorText={ID_number.error}
        keyboardType="numeric"
        
      />
      <Button
        mode="contained"
        onPress={onSignUpPressed}
        style={{ marginTop: 24 }}
      >
        Sign Up
      </Button>
      <View style={styles.row}>
        <Text>Already have an account? </Text>
        <TouchableOpacity onPress={() => navigation.replace('LoginScreen')}>
          <Text style={styles.link}>Login</Text>
        </TouchableOpacity>
      </View>
    </Background>
  )
}

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    marginTop: 4,
  },
  link: {
    fontWeight: 'bold',
    color: theme.colors.primary,
  }
})

