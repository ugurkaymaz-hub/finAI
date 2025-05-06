// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    plugins: [react()],
    server: {
        host: true, // Container dışından erişimi mümkün kılar
        port: 3000, // İçeride 3000 portunu dinle
    },
});
