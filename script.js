// DSA Solutions Data Structure
const dsaSolutions = {
    arrays: [
        { name: "Second Largest Element", file: "Array/Second-Largest-Element.py", language: "Python" },
        { name: "Move All Zeroes to End", file: "Array/Move-all-zeroes-to-end.py", language: "Python" },
        { name: "Reverse Array", file: "Array/Reverse-array.py", language: "Python" },
        { name: "Rotate Array", file: "Array/Rotate-array.py", language: "Python" },
        { name: "Next Permutation", file: "Array/Next-permutation.py", language: "Python" },
        { name: "Majority Element II", file: "Array/Majority Element II.py", language: "Python" },
        { name: "Stock Buy and Sell – Max one Transaction", file: "Array/Stock Buy and Sell – Max one Transaction Allowed.py", language: "Python" },
        { name: "Stock Buy and Sell – Multiple Transactions", file: "Array/Stock Buy and Sell – Multiple Transaction Allowed.py", language: "Python" },
        { name: "Maximum Subarray Sum - Kadane's Algorithm", file: "Array/Maximum Subarray Sum - Kadane's Algorithm.py", language: "Python" },
        { name: "Maximum Product Subarray", file: "Array/Maximum Product Subarray.py", language: "Python" },
        { name: "Maximum Circular Subarray Sum", file: "Array/Maximum Circular Subarray Sum.py", language: "Python" },
        { name: "Minimize the Heights II", file: "Array/Minimize the Heights II.py", language: "Python" },
        { name: "Find Smallest Missing Positive Number", file: "Array/Find Smallest Missing Positive Number.py", language: "Python" }
    ],
    strings: [
        { name: "Add Two Binary Strings", file: "String/Add two binary strings.py", language: "Python" },
        { name: "Check if Strings Are Rotations", file: "String/Check if Strings Are Rotations of Each Other.py", language: "Python" },
        { name: "Check if two Strings are Anagrams", file: "String/Check if two Strings are Anagrams of each other.py", language: "Python" },
        { name: "First Non-repeating Character", file: "String/First non-repeating character of given string.py", language: "Python" },
        { name: "KMP Algorithm for Pattern Searching", file: "String/KMP Algorithm for Pattern Searching.py", language: "Python" },
        { name: "Minimum Characters to Add at Front for Palindrome", file: "String/Minimum Characters to Add at Front for Palindrome.py", language: "Python" },
        { name: "String to Integer - atoi()", file: "String/String to Integer - Write your own atoi().py", language: "Python" }
    ],
    matrix: [
        { name: "Rotate Square Matrix by 90 Degrees", file: "Matrix/Rotate Square Matrix by 90 Degrees Counterclockwise.py", language: "Python" },
        { name: "Search in Row-wise and Column-wise Sorted Matrix", file: "Matrix/Search in a row wise and column wise sorted matrix.py", language: "Python" },
        { name: "Print Matrix in Spiral Form", file: "Matrix/Print a given matrix in spiral form.py", language: "Python" },
        { name: "Search in Row-wise Sorted Matrix", file: "Matrix/Search in row wise sorted matrix.py", language: "Python" },
        { name: "Set Matrix Rows and Columns to Zeroes", file: "Matrix/Set Matrix Rows and Columns to Zeroes.py", language: "Python" },
        { name: "Search Element in Sorted Matrix", file: "Matrix/Search element in a sorted matrix.py", language: "Python" }
    ],
    sorting: [
        { name: "Count Inversions of an Array", file: "Sorting/Count Inversions of an Array.py", language: "Python" },
        { name: "Insert and Merge Interval", file: "Sorting/Insert and Merge Interval.py", language: "Python" },
        { name: "Merge Overlapping Intervals", file: "Sorting/Merge Overlapping Intervals.py", language: "Python" },
        { name: "Sort an array of 0s, 1s and 2s", file: "Sorting/Sort an array of 0s, 1s and 2s - Dutch National Flag Problem.py", language: "Python" },
        { name: "H-Index", file: "Sorting/H-Index.py", language: "Python" },
        { name: "Merge Two Sorted Arrays Without Extra Space", file: "Sorting/Merge Two Sorted Arrays Without Extra Space.py", language: "Python" },
        { name: "Non-Overlapping Intervals", file: "Sorting/Non-Overlapping Intervals.py", language: "Python" }
    ]
};

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    loadAllProblems();
    setupSmoothScrolling();
});

// Load and display all problems
function loadAllProblems() {
    Object.keys(dsaSolutions).forEach(topic => {
        loadProblemsForTopic(topic);
    });
}

// Load problems for a specific topic
function loadProblemsForTopic(topic) {
    const container = document.getElementById(`${topic}-problems`);
    if (!container) return;

    const problems = dsaSolutions[topic];
    if (!problems || problems.length === 0) {
        container.innerHTML = '<p class="loading">No problems available yet.</p>';
        return;
    }

    container.innerHTML = problems.map(problem => createProblemCard(problem)).join('');
}

// Create a problem card HTML
function createProblemCard(problem) {
    const cleanName = problem.name.replace(/[^a-zA-Z0-9]/g, '');
    return `
        <div class="problem-card" onclick="toggleCode('${cleanName}')">
            <div class="problem-title">${problem.name}</div>
            <span class="problem-language">${problem.language}</span>
            <a href="https://github.com/Abhijit1018/GFG160/blob/main/${encodeURIComponent(problem.file)}" 
               target="_blank" 
               class="problem-link"
               onclick="event.stopPropagation()">
                <i class="fas fa-external-link-alt"></i> View on GitHub
            </a>
            <div id="code-${cleanName}" class="code-display">
                <div class="loading">Loading code...</div>
            </div>
        </div>
    `;
}

// Toggle code display
function toggleCode(problemId) {
    const codeDisplay = document.getElementById(`code-${problemId}`);
    if (!codeDisplay) return;

    if (codeDisplay.classList.contains('show')) {
        codeDisplay.classList.remove('show');
    } else {
        codeDisplay.classList.add('show');
        // If code hasn't been loaded yet, load it
        if (codeDisplay.innerHTML.includes('Loading code...')) {
            loadCode(problemId, codeDisplay);
        }
    }
}

// Load code from GitHub (this is a simplified version - in a real scenario you'd need proper API calls)
function loadCode(problemId, container) {
    // For now, we'll show a placeholder since we can't make direct API calls from GitHub Pages
    // In a real implementation, you'd use the GitHub API or have the code pre-loaded
    setTimeout(() => {
        container.innerHTML = `
            <pre><code class="language-python">
# Code for this problem
# Due to GitHub Pages limitations, the actual code cannot be fetched dynamically
# Please click "View on GitHub" to see the complete solution

def solution():
    """
    This is a placeholder for the actual solution.
    Click 'View on GitHub' above to see the complete code.
    """
    pass
            </code></pre>
            <p style="margin-top: 1rem; padding: 0.5rem; background: #e3f2fd; border-radius: 5px; font-size: 0.9rem;">
                <i class="fas fa-info-circle"></i> 
                Click "View on GitHub" above to see the complete solution with detailed comments and explanations.
            </p>
        `;
        
        // Highlight the code
        if (window.Prism) {
            window.Prism.highlightAll();
        }
    }, 500);
}

// Setup smooth scrolling for navigation
function setupSmoothScrolling() {
    const navLinks = document.querySelectorAll('.nav-list a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Add some interactive features
document.addEventListener('DOMContentLoaded', function() {
    // Add scroll-to-top functionality
    const scrollToTop = document.createElement('div');
    scrollToTop.innerHTML = '<i class="fas fa-chevron-up"></i>';
    scrollToTop.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: #667eea;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        opacity: 0;
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    `;
    
    document.body.appendChild(scrollToTop);
    
    // Show/hide scroll to top button
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollToTop.style.opacity = '1';
        } else {
            scrollToTop.style.opacity = '0';
        }
    });
    
    // Scroll to top functionality
    scrollToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Add some animation to cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all problem cards
    setTimeout(() => {
        const cards = document.querySelectorAll('.problem-card');
        cards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'all 0.6s ease';
            observer.observe(card);
        });
    }, 100);
});