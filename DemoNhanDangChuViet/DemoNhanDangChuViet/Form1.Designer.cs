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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // btInputImage
            // 
            this.btInputImage.Location = new System.Drawing.Point(12, 12);
            this.btInputImage.Name = "btInputImage";
            this.btInputImage.Size = new System.Drawing.Size(75, 23);
            this.btInputImage.TabIndex = 1;
            this.btInputImage.Text = "Input image";
            this.btInputImage.UseVisualStyleBackColor = true;
            this.btInputImage.Click += new System.EventHandler(this.btInputImage_Click);
            // 
            // btRead
            // 
            this.btRead.Location = new System.Drawing.Point(12, 386);
            this.btRead.Name = "btRead";
            this.btRead.Size = new System.Drawing.Size(75, 23);
            this.btRead.TabIndex = 2;
            this.btRead.Text = "Nhận Diện";
            this.btRead.UseVisualStyleBackColor = true;
            this.btRead.Click += new System.EventHandler(this.btRead_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(101, 388);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(482, 191);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // btImportExcel
            // 
            this.btImportExcel.Location = new System.Drawing.Point(600, 388);
            this.btImportExcel.Name = "btImportExcel";
            this.btImportExcel.Size = new System.Drawing.Size(75, 23);
            this.btImportExcel.TabIndex = 4;
            this.btImportExcel.Text = "Import Excel";
            this.btImportExcel.UseVisualStyleBackColor = true;
            this.btImportExcel.Click += new System.EventHandler(this.btImportExcel_Click);
            // 
            // btContour
            // 
            this.btContour.Location = new System.Drawing.Point(700, 7);
            this.btContour.Name = "btContour";
            this.btContour.Size = new System.Drawing.Size(75, 23);
            this.btContour.TabIndex = 6;
            this.btContour.Text = "Contour";
            this.btContour.UseVisualStyleBackColor = true;
            this.btContour.Click += new System.EventHandler(this.btContour_Click);
            // 
            // btReshape
            // 
            this.btReshape.Location = new System.Drawing.Point(600, 7);
            this.btReshape.Name = "btReshape";
            this.btReshape.Size = new System.Drawing.Size(75, 23);
            this.btReshape.TabIndex = 7;
            this.btReshape.Text = "Reshap Image";
            this.btReshape.UseVisualStyleBackColor = true;
            this.btReshape.Click += new System.EventHandler(this.btReshape_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(16, 17);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(534, 301);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            // 
            // panel1
            // 
            this.panel1.AutoScroll = true;
            this.panel1.Controls.Add(this.pictureBox1);
            this.panel1.Location = new System.Drawing.Point(12, 41);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(571, 333);
            this.panel1.TabIndex = 9;
            // 
            // panel2
            // 
            this.panel2.AutoScroll = true;
            this.panel2.Controls.Add(this.pictureBox2);
            this.panel2.Location = new System.Drawing.Point(600, 41);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(571, 333);
            this.panel2.TabIndex = 10;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(16, 19);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(534, 301);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox2.TabIndex = 8;
            this.pictureBox2.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1195, 604);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.btReshape);
            this.Controls.Add(this.btContour);
            this.Controls.Add(this.btImportExcel);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btRead);
            this.Controls.Add(this.btInputImage);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btInputImage;
        private System.Windows.Forms.Button btRead;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button btImportExcel;
        private System.Windows.Forms.Button btContour;
        private System.Windows.Forms.Button btReshape;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.PictureBox pictureBox2;
    }
}

