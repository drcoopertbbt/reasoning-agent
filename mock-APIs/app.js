const express = require('express');
const cors = require('cors');
const app = express();
const path = require('path');

// Enable CORS for all routes
app.use(cors());

// Middleware to handle JSON parsing
app.use(express.json());

// Helper function to serve JSON data
function serveJsonFile(filename) {
    return (req, res) => {
        try {
            const data = require(path.join(__dirname, filename));
            res.status(200).json(data);
        } catch (error) {
            console.error(`Error serving ${filename}:`, error);
            res.status(500).json({ message: "Internal Server Error", error: error.message });
        }
    };
}

// Define routes
app.get('/api/centralized-alarm', serveJsonFile('centralized_alarm_collection.json'));
app.get('/api/root-cause-analysis', serveJsonFile('root_cause_analysis.json'));
app.get('/api/automated-fault-detection', serveJsonFile('automated_fault_detection.json'));
app.get('/api/yang-models-fault-reporting', serveJsonFile('yang_models_fault_reporting.json'));
app.get('/api/alarm-logging-data-analysis', serveJsonFile('alarm_logging_data_analysis.json'));
app.get('/api/real-time-visualization', serveJsonFile('real_time_visualization.json'));
app.get('/api/collaborate-across-teams', serveJsonFile('collaborate_across_teams.json'));
app.get('/api/alarm-design-best-practices', serveJsonFile('alarm_design_best_practices.json'));

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: "Something went wrong!", error: err.message });
});

// Start the server
const PORT = process.env.PORT || 3005;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});