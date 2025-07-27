import os
from core.template_renderer import render_template
from core.format_docx import write_formatted_docx

def main():
    template_path = "configs/template.yaml.j2"
    values_path = "configs/data.yaml"
    output_dir = "output"
    output_txt = os.path.join(output_dir, "Generated_Test_Plan.txt")
    output_docx = os.path.join(output_dir, "Generated_Test_Plan.docx")

    if not os.path.exists(template_path):
        print(f"❌ Template file missing: {template_path}")
        return
    if not os.path.exists(values_path):
        print(f"❌ Values file missing: {values_path}")
        return

    print(f"➡️ Rendering template '{template_path}' with values '{values_path}'...")
    output_text = render_template(template_path, values_path)

    os.makedirs(output_dir, exist_ok=True)

    print(f"➡️ Writing output text file to '{output_txt}'...")
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"➡️ Writing output DOCX file to '{output_docx}'...")
    write_formatted_docx(output_text, output_docx)

    print(f"✅ Generation complete! Check files in '{output_dir}'.")

if __name__ == "__main__":
    main()
