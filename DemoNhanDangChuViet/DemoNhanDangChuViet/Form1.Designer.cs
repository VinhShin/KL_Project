namespace DemoNhanDangChuViet
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btInputImage = new System.Windows.Forms.Button();
            this.btRead = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.btImportExcel = new System.Windows.Forms.Button();
            this.btContour = new System.Windows.Forms.Button();
            this.btReshape = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btInputImage
            // 
            this.btInputImage.Location = new System.Drawing.Point(24, 49);
            this.btInputImage.Name = "btInputImage";
            this.btInputImage.Size = new System.Drawing.Size(75, 23);
            this.btInputImage.TabIndex = 1;
            this.btInputImage.Text = "Input image";
            this.btInputImage.UseVisualStyleBackColor = true;
            this.btInputImage.Click += new System.EventHandler(this.btInputImage_Click);
            // 
            // btRead
            // 
            this.btRead.Location = new System.Drawing.Point(311, 49);
            this.btRead.Name = "btRead";
            this.btRead.Size = new System.Drawing.Size(75, 23);
            this.btRead.TabIndex = 2;
            this.btRead.Text = "Read file";
            this.btRead.UseVisualStyleBackColor = true;
            this.btRead.Click += new System.EventHandler(this.btRead_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(311, 107);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(223, 154);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // btImportExcel
            // 
            this.btImportExcel.Location = new System.Drawing.Point(402, 49);
            this.btImportExcel.Name = "btImportExcel";
            this.btImportExcel.Size = new System.Drawing.Size(75, 23);
            this.btImportExcel.TabIndex = 4;
            this.btImportExcel.Text = "Import Excel";
            this.btImportExcel.UseVisualStyleBackColor = true;
            this.btImportExcel.Click += new System.EventHandler(this.btImportExcel_Click);
            // 
            // btContour
            // 
            this.btContour.Location = new System.Drawing.Point(217, 49);
            this.btContour.Name = "btContour";
            this.btContour.Size = new System.Drawing.Size(75, 23);
            this.btContour.TabIndex = 6;
            this.btContour.Text = "Contour";
            this.btContour.UseVisualStyleBackColor = true;
            this.btContour.Click += new System.EventHandler(this.btContour_Click);
            // 
            // btReshape
            // 
            this.btReshape.Location = new System.Drawing.Point(117, 48);
            this.btReshape.Name = "btReshape";
            this.btReshape.Size = new System.Drawing.Size(75, 23);
            this.btReshape.TabIndex = 7;
            this.btReshape.Text = "Reshap Image";
            this.btReshape.UseVisualStyleBackColor = true;
            this.btReshape.Click += new System.EventHandler(this.btReshape_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(660, 423);
            this.Controls.Add(this.btReshape);
            this.Controls.Add(this.btContour);
            this.Controls.Add(this.btImportExcel);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btRead);
            this.Controls.Add(this.btInputImage);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btInputImage;
        private System.Windows.Forms.Button btRead;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button btImportExcel;
        private System.Windows.Forms.Button btContour;
        private System.Windows.Forms.Button btReshape;
    }
}

