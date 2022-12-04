// import CSS
import Button from "@mui/material/Button";
import ButtonGroup from "@mui/material/ButtonGroup";
import Box from "@mui/material/Box";
import { Link, Stack } from "@mui/material";

export default function Landing_Page() {
  return (
    <div>
      <Stack spacing={1} alignItems="flex-end">
        <Link>Sign In</Link>
        <Link>Register</Link>
      </Stack>

      <h1>Codeunity</h1>
      <h2>Work Play Communicate</h2>
    </div>
  );
}
