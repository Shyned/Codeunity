// import CSS
import Button from "@mui/material/Button";
import ButtonGroup from "@mui/material/ButtonGroup";
import Box from "@mui/material/Box";
import { Stack } from "@mui/material";
import { Link } from "react-router-dom";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

export default function Landing_Page() {
  const darkTheme = createTheme({
    palette: {
      mode: "dark",
    },
  });

  const LightTheme = createTheme({
    palette: {
      mode: "light",
    },
  });

  return (
    <div>
      <ThemeProvider theme={LightTheme}>
        <CssBaseline />
        <main>This app is using the dark mode</main>
      </ThemeProvider>
      <Stack spacing={2} alignItems="flex-end">
        <Link to="login/">Sign In</Link>
        <Link to="signup/">Register</Link>
      </Stack>
      <h1>Codeunity</h1>
      <h2>Work Play Communicate</h2>
    </div>
  );
}
