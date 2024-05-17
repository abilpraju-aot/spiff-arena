import react from "@vitejs/plugin-react";
import { defineConfig, transformWithEsbuild } from "vite";

/*
  custom plugin to transform js to jsx
*/
const jsToJsx = () => {
  return {
    name: "treat-js-files-as-jsx",
    async transform(code, id) {
      if (!id.match(/src\/.*\.js$/)) return null;

      // Use the exposed transform from vite, instead of directly
      // transforming with esbuild
      return transformWithEsbuild(code, id, {
        loader: "jsx",
        jsx: "automatic",
      });
    },
  };
};

export default defineConfig({
  build: {
    rollupOptions: {
      input: "src/index.js",
      preserveEntrySignatures: "exports-only",
      output: {
        exports: "auto",
        format: "amd",
        entryFileNames: "forms-flow-spliff.js",
      },
    },
  },
  plugins: [react(), jsToJsx()],
  server: {
    host: "localhost",
    port: "7001",
  },
});