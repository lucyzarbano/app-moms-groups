# Moms Groups Frontend

Scaffolding iniziale React Native per l'app mobile Moms Groups.

## Struttura

- `src/api`: client HTTP e funzioni API
- `src/components`: componenti UI riutilizzabili
- `src/config`: configurazioni applicative
- `src/context`: stato globale leggero
- `src/navigation`: navigazione applicativa
- `src/screens`: schermate principali MVP
- `src/types`: tipi condivisi

## Prossimo step

Scegliere il bootstrap concreto tra Expo e React Native CLI. Per un MVP con push notification, Expo e' una buona opzione iniziale se non servono moduli nativi custom.

## Avvio Metro

Da PowerShell:

```powershell
cd C:\Users\LuciaZarbano\Desktop\STUDY\Moms\app-moms-groups\frontend
npm install
npm start
```

Questo avvia Metro, il bundler di React Native.

Nota: questa cartella contiene ancora uno scaffolding iniziale. Per visualizzare l'app su emulatore o telefono servira' completare il bootstrap nativo con Expo o React Native CLI.
