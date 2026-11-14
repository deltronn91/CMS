const conceptList = document.getElementById("concept-list");

const conceptDetail = document.createElement("div");
conceptDetail.id = "concept-detail";
conceptList.after(conceptDetail);

async function loadConcepts() {
    conceptList.textContent = "Loading concepts...";

    try {
        const response = await fetch("/concepts");

        if (!response.ok) { 
            throw new Error("Failed to load concepts");
        }

        const concepts = await response.json();

        conceptList.replaceChildren();

        if (concepts.length === 0) {
            conceptList.textContent = "No concepts available yet.";
            return;
        }

        concepts.forEach(concept => {
            const button = document.createElement("button");
            button.textContent = concept.title;
            ///closure is what gives my buttons access to the concept.id after being called
            button.addEventListener("click", () => {
                loadConceptDetail(concept.id);
            });

            conceptList.appendChild(button);
        });

    } catch (error) {
        conceptList.textContent = "Could not load concepts.";
        console.error(error);
    }
}

async function loadConceptDetail(conceptId) {
    conceptDetail.textContent = "Loading concept...";

    try {
        const response = await fetch(`/concepts/${conceptId}`);

        if (!response.ok) {
            throw new Error("Failed to load concept");
        }

        const concept = await response.json();

        conceptDetail.replaceChildren();
        // Clear the existing contents of conceptDetail.
        
        // Create a heading to display the selected concept's title
        // and prepare to display its fields.
        const title = document.createElement("h2");
        title.textContent = concept.title;
        conceptDetail.appendChild(title);
        //every concept has these corresponding fields
        const fields = [
            ["Definition", concept.definition],
            ["Example", concept.example],
            ["Explanation", concept.explanation],
            ["Common misconception", concept.common_misconception],
            ["Related concepts", concept.related_concepts]
        ];

        fields.forEach(([label, value]) => {
            if (value == null || value === "") return;

            const heading = document.createElement("h3");
            heading.textContent = label;

            const paragraph = document.createElement("p");
            paragraph.textContent = value

            conceptDetail.append(heading, paragraph);
        });

    } catch (error) {
        conceptDetail.textContent = "Could not load this concept.";
        console.error(error);
    }
}

loadConcepts();

