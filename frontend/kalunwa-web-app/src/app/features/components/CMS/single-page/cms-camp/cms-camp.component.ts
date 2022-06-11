import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ImageSnippet } from 'src/app/admin/model/collective-page-model';
import { SinglePageService } from 'src/app/features/service/single-page.service';

@Component({
  selector: 'app-cms-camp',
  templateUrl: './cms-camp.component.html',
  styleUrls: ['./cms-camp.component.scss']
})
export class CmsCampComponent implements OnInit {

  campName: string | null='baybayon';
  page: FormGroup;
  submitted= false;
  headerFileName="";
  contentFileName="";
  selectedFile: ImageSnippet;

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private service: SinglePageService,
  ) { }

  ngOnInit(): void {
    this.page = this.formBuilder.group({
      description: ['',Validators.required],
      header_image: [null],
      content_image: [null],
    });

    this.campName = this.route.snapshot.paramMap.get("camp-type");
  }

  get f() { return this.page.controls;}

  onSubmit(imageInput1:any,imageInput2:any){
    this.submitted = true;

    console.log(this.page.value);
    console.log("------");
    console.log("+++++++");
    console.log(this.f.image.value);

    if(this.page.invalid){
      return;
    }
    else{
      this.service.updateCamp();
    }
  }

  onFileChange(imageInput:any){
    const file: File = imageInput.files[0];
    const reader = new FileReader();
    if(!this.isFileImage(file)){
      this.page.controls["header_image"].setErrors({'incorrect': true});
      this.page.controls["content_image"].setErrors({'incorrect': true});
    }
    else if (this.isFileImage(file) && imageInput.name=="header_image"){
      this.headerFileName = file.name;
    }
    else if (this.isFileImage(file) && imageInput.name=="content_image"){
      this.contentFileName = file.name;
    }
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    if(this.isFileImage(file)){

      reader.addEventListener('load', (event: any) => {

        this.selectedFile = new ImageSnippet(event.target.result, file);

        this.service.uploadImage(this.headerFileName,file).subscribe(
          (res) => {
          },
          (err) => {

        })
        this.service.uploadImage(this.contentFileName,file).subscribe(
          (res) => {
          },
          (err) => {

        })
      });

      reader.readAsDataURL(file);
    }
    else{

    }
  }
  isFileImage(file: File) {
    return file && file['type'].split('/')[0] === 'image';
  }

  displayDate(date: Date){
    if(!date)
      return "";
    return this.service.printDate(date);
  }

}
