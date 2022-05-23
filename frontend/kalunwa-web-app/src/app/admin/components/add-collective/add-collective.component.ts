import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { ImageSnippet } from '../../model/collective-page-model';
import { CollectivePagesService } from '../../service/collective-pages.service';

@Component({
  selector: 'app-add-collective',
  templateUrl: './add-collective.component.html',
  styleUrls: ['./add-collective.component.scss']
})
export class AddCollectiveComponent implements OnInit {
  isAdd = true;
  collective: FormGroup;
  submitted= false;
  collectiveType: string | null= "project";
  status = "";
  fileName=""
  selectedFile: ImageSnippet;
  collection:any;


  constructor(
    private formBuilder: FormBuilder,
    private service: CollectivePagesService,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
      this.collective = this.formBuilder.group({
      title: ['',Validators.required],
      start_date: [null],
      end_date: [null],
      camp: ['',Validators.required],
      description: ['',Validators.required],
      image:[null]
    });

    const collectiveId = this.route.snapshot.paramMap.get("id");
    console.log(collectiveId);
    if(collectiveId == "")
      this.isAdd = true;
    else
      this.isAdd = false;

    this.collectiveType = this.route.snapshot.paramMap.get("collective-type");

    if(!this.isAdd){
      if(this.collectiveType == "project"){
            this.service.getProjectDetails(collectiveId)
                .pipe(first())
                .subscribe(x => this.collective.patchValue(x));
      }
      else if(this.collectiveType == "event"){
        this.service.getEventDetails(collectiveId)
            .pipe(first())
            .subscribe(x => this.collective.patchValue(x));
      }
      else if(this.collectiveType == "news"){
        this.service.getNewsDetails(collectiveId)
            .pipe(first())
            .subscribe(x => this.collective.patchValue(x));
      }
    }
  }

  get f() { return this.collective.controls;}

  onSubmit(imageInput:any){
    this.submitted = true;

    console.log(this.collective.value);
    console.log("------");
    console.log("+++++++");
    console.log(this.f.image.value);

    if(this.collective.invalid){
      return;
    }

    if(this.isAdd){
      this.processFile(imageInput);
      this.createCollective();
    }
    else{
      this.updateCollective();
    }

  }

  private createCollective(){
    if(this.collectiveType=="project"){
      this.service.addProject();
    }
    if(this.collectiveType=="event"){
      this.service.addEvent();
    }
    if(this.collectiveType=="news"){
      this.service.addNews();
    }
  }

  private updateCollective(){
    if(this.collectiveType=="project"){
      this.service.updateProject();
    }
    if(this.collectiveType=="event"){
      this.service.updateEvent();
    }
    if(this.collectiveType=="news"){
      this.service.updateNews();
    }
  }

  updateStatus(){
    let now = new Date();
    console.log(this.f.start_date.value, this.f.end_date.value);
    if(this.f.start_date.value != null && this.f.end_date.value != null){
      if(this.f.start_date.value > now){
        this.status="Upcoming";
        if(this.f.start_date.value > this.f.endDate.value)
          this.collective.controls["end_date"].setErrors({'incorrect': true});
        else
          this.collective.controls["end_date"].setErrors(null);
      }
      else{
        this.status="Ongoing";
        if(this.f.end_date.value < now )
          this.status="Past";

        if(this.f.start_date.value > this.f.end_date.value)
          this.collective.controls["end_date"].setErrors({'incorrect': true});
        else
          this.collective.controls["end_date"].setErrors(null);
      }
    }
  }

  onFileChange(imageInput:any){
    const file: File = imageInput.files[0];
    const reader = new FileReader();
    if(!this.isFileImage(file))
      this.collective.controls["image"].setErrors({'incorrect': true});
    else{
      this.collective.controls["image"].setErrors(null);

      this.fileName = file.name;
    }
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    if(this.isFileImage(file)){

      reader.addEventListener('load', (event: any) => {

        this.selectedFile = new ImageSnippet(event.target.result, file);

        this.service.uploadImage(this.fileName,file).subscribe(
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
