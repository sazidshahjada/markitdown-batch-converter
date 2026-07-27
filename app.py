import os
import io
import zipfile
import streamlit as st
from markitdown import MarkItDown


# Set up page layout
st.set_page_config(page_title="Batch Doc to Markdown", page_icon="📚", layout="centered")

st.title("📚 Batch Document to Markdown")
st.write("Upload multiple documents to convert them all to Markdown simultaneously.")

# Initialize the MarkItDown tool
@st.cache_resource
def get_converter():
    return MarkItDown()

md_converter = get_converter()

# Multi-file uploader widget (accepts PDF, Docx, Xlsx, Pptx)
uploaded_files = st.file_uploader(
    "Choose files to convert", 
    type=["pdf", "docx", "xlsx", "pptx", "txt"], 
    accept_multiple_files=True
)

# Process only if files are uploaded
if uploaded_files:
    st.info(f"📂 Total files selected: **{len(uploaded_files)}**")
    
    # Trigger batch conversion on button click
    if st.button("🚀 Convert All Files", use_container_width=True):
        
        # Create an in-memory byte buffer to hold our ZIP archive
        zip_buffer = io.BytesIO()
        
        # Track processing statuses
        success_count = 0
        error_count = 0
        
        # Initialize an explicit progress bar UI component
        progress_bar = st.progress(0.0)
        status_text = st.empty()
        
        # Open the ZIP archive structure in write mode
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            
            for index, uploaded_file in enumerate(uploaded_files):
                # Update progress tracking UI metrics
                current_progress = (index) / len(uploaded_files)
                progress_bar.progress(current_progress)
                status_text.text(f"Processing ({index + 1}/{len(uploaded_files)}): {uploaded_file.name}")
                
                try:
                    # Save a temporary copy locally to pass clean paths to MarkItDown
                    temp_filename = f"temp_{uploaded_file.name}"
                    with open(temp_filename, "wb") as f:
                        f.write(uploaded_file.read())
                    
                    # Core file structural conversion execution
                    result = md_converter.convert(temp_filename)
                    markdown_text = result.text_content
                    
                    # Clean up file copy from Ubuntu hard drive immediately
                    if os.path.exists(temp_filename):
                        os.remove(temp_filename)
                    
                    # Generate identical output file name swapping out old extension
                    base_name = os.path.splitext(uploaded_file.name)[0]
                    output_md_filename = f"{base_name}.md"
                    
                    # Write the converted string directly as a file inside the zip archive
                    zip_file.writestr(output_md_filename, markdown_text)
                    success_count += 1
                    
                except Exception as e:
                    error_count += 1
                    st.error(f"❌ Failed to convert {uploaded_file.name}: {str(e)}")
            
            # Finalize progress reporting assets
            progress_bar.progress(1.0)
            status_text.text("Batch job completed!")
            
        # Display completion summary notifications 
        if success_count > 0:
            st.success(f"🎉 Successfully converted {success_count} file(s)!")
            
            # Reset zip pointer to position zero for streaming out to user browser
            zip_buffer.seek(0)
            
            # Provide single macro action button to download the entire bulk output package
            st.download_button(
                label="📥 Download All Converted Files (.ZIP)",
                data=zip_buffer.getvalue(),
                file_name="converted_markdown_documents.zip",
                mime="application/zip",
                use_container_width=True,
                type="primary"
            )
            
        if error_count > 0:
            st.warning(f"⚠️ Completed with {error_count} processing exception failures.")
