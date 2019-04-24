from django.contrib import adminfrom attivita.models import Partecipazione, Turno, Area, Attivitafrom base.admin import InlineAutorizzazionefrom gruppi.readonly_admin import ReadonlyAdminMixinfrom attivita.models import NonSonoUnBersagliofrom django.contrib import messages__author__ = 'alfioemanuele'@admin.register(Attivita)class AdminAttivita(ReadonlyAdminMixin, admin.ModelAdmin):    search_fields = ['nome', 'sede__nome', 'estensione__nome', 'area__nome']    list_display = ('nome', 'sede', 'area', 'estensione', 'stato', 'apertura')    list_filter = ('creazione', 'stato', 'apertura')    raw_id_fields = ('locazione', 'sede', 'estensione', 'area', )@admin.register(Area)class AdminArea(ReadonlyAdminMixin, admin.ModelAdmin):    search_fields = ['nome', 'sede__nome', 'obiettivo']    list_display = ('nome', 'sede', 'obiettivo', 'creazione')    list_filter = ('creazione', 'obiettivo')    raw_id_fields = ('sede',)@admin.register(Turno)class AdminTurno(ReadonlyAdminMixin, admin.ModelAdmin):    search_fields = ['nome', 'attivita__nome', 'attivita__sede__nome',]    list_display = ('nome', 'attivita', 'inizio', 'fine', 'creazione', )    list_filter = ('inizio', 'fine', 'creazione',)    raw_id_fields = ('attivita',)@admin.register(Partecipazione)class AdminPartecipazione(ReadonlyAdminMixin, admin.ModelAdmin):    search_fields = ['persona__codice_fiscale', 'persona__cognome', 'persona__nome', 'turno__nome', 'turno__attivita__nome',]    list_display = ('turno', 'persona', 'creazione', 'esito',)    list_filter = ('creazione', 'stato', 'confermata',)    raw_id_fields = ('persona', 'turno', )    inlines = [InlineAutorizzazione]import csv@admin.register(NonSonoUnBersaglio)class AdminNonSonoUnBersaglio(ReadonlyAdminMixin, admin.ModelAdmin):    search_fields = ['persona__codice_fiscale', 'persona__cognome', 'persona__nome', ]    list_display = ('persona', 'centro_formazione', )    raw_id_fields = ('persona', )    def carica_referenti(self, request, file):        # messages.success(request, "File caricato correttamente {}".format(file.name))        fieldnames = (            'Email',            'Centro di Formazione',            'Nome',            'Cognome',            'Codice Fiscale',        )        import io        from anagrafica.models import Persona        reader = csv.DictReader(io.StringIO(file.read().decode('utf-8')), delimiter=',', fieldnames=fieldnames)        referenti = []        referrenti_non_trovati = []        next(reader)        for row in reader:            query = {}            if row['Email']:                query['email_contatto'] = row['Email']            if row['Nome']:                query['nome'] = row['Nome']            if row['Cognome']:                query['cognome'] = row['Cognome']            if row['Codice Fiscale']:                query['codice_fiscale'] = row['Codice Fiscale']            persona = Persona.objects.filter(**query)            if len(persona) > 1:                messages.error(request, "Il file contiene valori ambigui su {}".format(persona))                return            if persona:                referenti.append({'persona': persona[0], 'centro': row['Centro di Formazione']})            else:                referrenti_non_trovati.append('{} {} {}'.format(row['Nome'], row['Cognome'], row['Codice Fiscale']))        for ref in referenti:            if not NonSonoUnBersaglio.objects.filter(persona=ref['persona']):                print('Non Esiste', ref['persona'])                referente = NonSonoUnBersaglio(persona=ref['persona'], centro_formazione=ref['centro'])                referente.save()        for ref in referrenti_non_trovati:            messages.warning(request, 'Referente {} non trovato'.format(ref))    def changelist_view(self, request, extra_context=None):        if request.POST:            files = request.FILES.getlist('file')            for file in files:                if not file.name.split('.')[1] == 'csv':                    messages.error(request, "Il file deve avere un fomato .csv")                    return super(AdminNonSonoUnBersaglio, self).changelist_view(request, extra_context=extra_context)            self.carica_referenti(request, files[0])        return super(AdminNonSonoUnBersaglio, self).changelist_view(request, extra_context=extra_context)