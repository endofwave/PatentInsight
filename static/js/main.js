// PatentInsight Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // MathJax configuration for dynamic content
    if (window.MathJax) {
        MathJax.typesetPromise();
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Auto-refresh MathJax when content loads dynamically
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList' && window.MathJax) {
                MathJax.typesetPromise();
            }
        });
    });
    
    // Observe content sections for changes
    const contentSections = document.querySelectorAll('.content-section');
    contentSections.forEach(section => {
        observer.observe(section, { childList: true, subtree: true });
    });
});

// Simulation management
class SimulationManager {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.isRunning = false;
    }
    
    showLoading() {
        if (this.container) {
            const loadingDiv = this.container.querySelector('#simulationLoading');
            const resultsDiv = this.container.querySelector('#simulationResults');
            const errorDiv = this.container.querySelector('#simulationError');
            
            if (loadingDiv) loadingDiv.classList.remove('d-none');
            if (resultsDiv) resultsDiv.classList.add('d-none');
            if (errorDiv) errorDiv.classList.add('d-none');
        }
    }
    
    showResults(data) {
        if (this.container) {
            const loadingDiv = this.container.querySelector('#simulationLoading');
            const resultsDiv = this.container.querySelector('#simulationResults');
            const outputPre = this.container.querySelector('#simulationOutput');
            const plotsDiv = this.container.querySelector('#simulationPlots');
            
            if (loadingDiv) loadingDiv.classList.add('d-none');
            if (resultsDiv) resultsDiv.classList.remove('d-none');
            
            if (outputPre && data.output) {
                outputPre.textContent = data.output;
            }
            
            if (plotsDiv && data.plots) {
                plotsDiv.innerHTML = '';
                data.plots.forEach((plotData, index) => {
                    const img = document.createElement('img');
                    img.src = 'data:image/png;base64,' + plotData;
                    img.className = 'simulation-plots img-fluid mb-3';
                    img.alt = `Simulation Plot ${index + 1}`;
                    img.loading = 'lazy';
                    plotsDiv.appendChild(img);
                });
            }
        }
    }
    
    showError(message) {
        if (this.container) {
            const loadingDiv = this.container.querySelector('#simulationLoading');
            const errorDiv = this.container.querySelector('#simulationError');
            
            if (loadingDiv) loadingDiv.classList.add('d-none');
            if (errorDiv) {
                errorDiv.textContent = message;
                errorDiv.classList.remove('d-none');
            }
        }
    }
}

// Initialize simulation managers on page load
document.addEventListener('DOMContentLoaded', function() {
    const simulationContainers = document.querySelectorAll('.simulation-section');
    simulationContainers.forEach(container => {
        const manager = new SimulationManager(container.id);
        
        const runButton = container.querySelector('#runSimulationBtn');
        const resetButton = container.querySelector('#resetSimulationBtn');
        
        if (runButton) {
            runButton.addEventListener('click', function() {
                manager.showLoading();
                // Simulation run logic would be handled by the template's inline JavaScript
            });
        }
        
        if (resetButton) {
            resetButton.addEventListener('click', function() {
                manager.showResults({output: '', plots: []});
            });
        }
    });
});
