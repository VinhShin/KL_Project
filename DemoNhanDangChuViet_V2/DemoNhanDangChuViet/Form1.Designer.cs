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
            this.label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // btInputImage
            // 
            this.btInputImage.BackColor = System.Drawing.SystemColors.Highlight;
            this.btInputImage.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btInputImage.ForeColor = System.Drawing.SystemColors.Control;
            this.btInputImage.Location = new System.Drawing.Point(25, 94);
            this.btInputImage.Name = "btInputImage";
            this.btInputImage.Size = new System.Drawing.Size(133, 40);
            this.btInputImage.TabIndex = 1;
            this.btInputImage.Text = "Chọn Ảnh";
            this.btInputImage.UseVisualStyleBackColor = false;
            this.btInputImage.Click += new System.EventHandler(this.btInputImage_Click);
            // 
            // btRead
            // 
            this.btRead.BackColor = System.Drawing.SystemColors.Highlight;
            this.btRead.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btRead.ForeColor = System.Drawing.SystemColors.Control;
            this.btRead.Location = new System.Drawing.Point(25, 468);
            this.btRead.Name = "btRead";
            this.btRead.Size = new System.Drawing.Size(94, 52);
            this.btRead.TabIndex = 2;
            this.btRead.Text = "Nhận Diện";
            this.btRead.UseVisualStyleBackColor = false;
            this.btRead.Click += new System.EventHandler(this.btRead_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(125, 470);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(493, 191);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // btImportExcel
            // 
            this.btImportExcel.BackColor = System.Drawing.SystemColors.Highlight;
            this.btImportExcel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btImportExcel.ForeColor = System.Drawing.SystemColors.Control;
            this.btImportExcel.Location = new System.Drawing.Point(649, 470);
            this.btImportExcel.Name = "btImportExcel";
            this.btImportExcel.Size = new System.Drawing.Size(122, 50);
            this.btImportExcel.TabIndex = 4;
            this.btImportExcel.Text = "Import Excel";
            this.btImportExcel.UseVisualStyleBackColor = false;
            this.btImportExcel.Click += new System.EventHandler(this.btImportExcel_Click);
            // 
            // btContour
            // 
            this.btContour.BackColor = System.Drawing.SystemColors.Highlight;
            this.btContour.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btContour.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.btContour.Location = new System.Drawing.Point(851, 89);
            this.btContour.Name = "btContour";
            this.btContour.Size = new System.Drawing.Size(135, 45);
            this.btContour.TabIndex = 6;
            this.btContour.Text = "Tách Nội Dung";
            this.btContour.UseVisualStyleBackColor = false;
            this.btContour.Click += new System.EventHandler(this.btContour_Click);
            // 
            // btReshape
            // 
            this.btReshape.BackColor = System.Drawing.SystemColors.Highlight;
            this.btReshape.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btReshape.ForeColor = System.Drawing.SystemColors.Control;
            this.btReshape.Location = new System.Drawing.Point(649, 89);
            this.btReshape.Name = "btReshape";
            this.btReshape.Size = new System.Drawing.Size(186, 45);
            this.btReshape.TabIndex = 7;
            this.btReshape.Text = "Điều Chỉnh Biên Ảnh";
            this.btReshape.UseVisualStyleBackColor = false;
            this.btReshape.Click += new System.EventHandler(this.btReshape_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(14, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(557, 284);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            // 
            // panel1
            // 
            this.panel1.AutoScroll = true;
            this.panel1.Controls.Add(this.pictureBox1);
            this.panel1.Location = new System.Drawing.Point(25, 140);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(593, 313);
            this.panel1.TabIndex = 9;
            // 
            // panel2
            // 
            this.panel2.AutoScroll = true;
            this.panel2.Controls.Add(this.pictureBox2);
            this.panel2.Location = new System.Drawing.Point(649, 140);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(610, 313);
            this.panel2.TabIndex = 10;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(18, 12);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(573, 284);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox2.TabIndex = 8;
            this.pictureBox2.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 26F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.label1.Location = new System.Drawing.Point(287, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(736, 39);
            this.label1.TabIndex = 11;
            this.label1.Text = "Ứng dụng demo nhận diện bảng điểm sinh viên";
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.SystemColors.Highlight;
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.ForeColor = System.Drawing.SystemColors.Control;
            this.button1.Location = new System.Drawing.Point(181, 94);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(148, 40);
            this.button1.TabIndex = 12;
            this.button1.Text = "Tách Vùng Điểm";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.LightBlue;
            this.ClientSize = new System.Drawing.Size(1279, 672);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label1);
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
            this.PerformLayout();

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
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button1;
    }
}

