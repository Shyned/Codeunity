import { KeyboardAvoidingView, TouchableOpacity } from "react-native";
import { TextInput } from "react-native-paper";

export default function LoginPage() {
  return;
  <KeyboardAvoidingView style={styles.container} behavior="padding">
    <view style={style.inputContainer}>
      <TextInput placeholder="Username" />
    </view>
    <view style={style.inputContainer}>
      <TextInput placeholder="Password" secureTextEntry />
    </view>
    <view style={style.button}>
      <TouchableOpacity onpress={() => {}}>
        <text style={style.button}>Login</text>
      </TouchableOpacity>
    </view>
  </KeyboardAvoidingView>;
}

const style = StyleSheet.create({
  container: {
    flex: 1,
    justifycontent: "center",
    alignItems: "center",
  },
});
