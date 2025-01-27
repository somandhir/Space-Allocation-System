const express = require('express');
const multer = require('multer');
const path = require('path');

// Initialize Express app
const app = express();
const port = 3000;

// Set up multer storage configuration
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');  // Specify the 'uploads' folder as the destination
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname)); // Unique filename with extension
  }
});

const upload = multer({ storage: storage });

// Serve static files (e.g., your front-end HTML)
app.use(express.static('public'));
  app.get('/baseStyling.css', (req, res) => {
    res.type('text/css');
    res.sendFile(path.join(__dirname, 'public', 'baseStyling.css'));
  });
  
// Route to handle file upload
app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }
  res.send(`File uploaded successfully: ${req.file.filename}`);
});

// Create an uploads folder if it doesn't exist
const fs = require('fs');
const uploadsDir = './uploads';
if (!fs.existsSync(uploadsDir)) {
  fs.mkdirSync(uploadsDir);
}

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
