import { useState } from "react";

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = (e) => {
        e.preventDefault(); // Sayfanın yenilenmesini engeller
        console.log("Giriş Bilgileri:", { username, password });

        // Buraya istersen backend'e gönderilecek login isteğini ekleyebilirsin
    };

    const handleForgotPassword = () => {
        // Şifre sıfırlama için yapılacak işlemleri buraya ekleyebilirsin
        console.log("Şifremi unuttum linkine tıklandı");
    };

    return (
        <div style={styles.container}>
            <h2>Giriş Yap</h2>
            <form onSubmit={handleLogin} style={styles.form}>
                <input
                    type="text"
                    placeholder="Kullanıcı Adı"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                    style={styles.input}
                />
                <input
                    type="password"
                    placeholder="Şifre"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    style={styles.input}
                />
                <button type="submit" style={styles.button}>
                    Giriş Yap
                </button>
            </form>

            <p style={styles.forgotPassword} onClick={handleForgotPassword}>
                Şifremi Unuttum
            </p>
        </div>
    );
}

// Basit stil tanımları
const styles = {
    container: {
        display: "flex", // Flexbox kullanarak hizalama yapıyoruz
        justifyContent: "center", // Yatayda ortalama
        alignItems: "center", // Dikeyde ortalama
        height: "50vh", // Sayfanın tamamını kaplayacak şekilde
        flexDirection: "column", // İçeriklerin dikey sırayla yerleşmesini sağlıyoruz
        padding: 20,
        border: "1px solid #ccc",
        borderRadius: 8,
        textAlign: "center",
    },
    form: {
        display: "flex",
        flexDirection: "column",
        gap: 12,
    },
    input: {
        padding: 10,
        fontSize: 16,
    },
    button: {
        padding: 10,
        fontSize: 16,
        backgroundColor: "#007bff",
        color: "white",
        border: "none",
        borderRadius: 4,
        cursor: "pointer",
    },
    forgotPassword: {
        marginTop: 12,
        color: "#007bff",
        cursor: "pointer",
    },
};

export default Login;
