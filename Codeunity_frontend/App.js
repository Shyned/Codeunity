import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";
// Imported components
import Navbar from "./components/Navbar/Navbar";
// imported pages
import HomePage from "./pages/HomePage/HomePage";
import ChatPage from "./pages/ChatPage/ChatPage";
import LoginPage from "./pages/LoginPage/LoginPage";
import SignUpPage from "./pages/SignUpPage/SignUpPage";
//
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

export default function App() {
  const Stack = createNativeStackNavigator();
  const hasUser = false;

  const coditionalElementifUser = (
    <Stack.Screen
      name="Chatroom"
      component={ChatPage}
      options={{ tite: "Room" }}
    />
  );

  const coditionalElementifNoUser = (
    <Stack.Screen
      name="Login"
      component={LoginPage}
      options={{ title: ":Login" }}
    />
  );
  return (
    <>
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen
            name="Login"
            component={LoginPage}
            options={{ tite: "login" }}
          />
          <Stack.Screen
            name="signup"
            component={SignUpPage}
            options={{ tite: "Welcome" }}
          />
          <Stack.Screen
            name="Home"
            component={HomePage}
            options={{ tite: "Welcome" }}
          />

          <Stack.Screen
            name="Navbar"
            component={Navbar}
            options={{ tite: "Navbar" }}
          />
        </Stack.Navigator>
      </NavigationContainer>
      <Navbar />
    </>
  );
}
