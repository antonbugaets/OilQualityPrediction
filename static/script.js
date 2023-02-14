    async function send(){


        const a = document.getElementById("a").value;
        const b = document.getElementById("b").value;
        const c = document.getElementById("c").value;
        const d = document.getElementById("d").value;

        const response = await fetch("/oil", {
                method: "POST",
                headers: { "Accept": "application/json", "Content-Type": "application/json" },
                body: JSON.stringify({
                    a: a,
                    b: b,
                    c: c,
                    d: d
                })
            });
            if (response.ok) {
                const data = await response.json();
                document.getElementById("message").textContent = data.message;
            }
            else
                console.log(response);
    }