async function analyzeText() {
    const textInput = document.getElementById('textInput').value;

    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: textInput }),
    });

    const result = await response.json();

    const resultDiv = document.getElementById('result');
    if (response.ok) {
        resultDiv.innerHTML = JSON.stringify(result, null, 2);
    } else {
        resultDiv.innerHTML = `<p style="color: red;">${result.error}</p>`;
    }
}
